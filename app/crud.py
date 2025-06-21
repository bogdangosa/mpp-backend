from typing import List, Optional
from datetime import datetime
from .models import Candidate
from .database import candidates_db, get_next_id

def get_candidates(skip: int = 0, limit: int = 100) -> List[Candidate]:
    """Get all candidates with pagination"""
    return candidates_db[skip : skip + limit]

def get_candidate(candidate_id: int) -> Optional[Candidate]:
    """Get a candidate by ID"""
    for candidate in candidates_db:
        if candidate.id == candidate_id:
            return candidate
    return None

def create_candidate(name: str, image: str, political_party: str, description: str) -> Candidate:
    """Create a new candidate"""
    candidate = Candidate(
        id=get_next_id(),
        name=name,
        image=image,
        politicalParty=political_party,
        description=description,
        createdAt=datetime.now(),
        updatedAt=None
    )
    candidates_db.append(candidate)
    return candidate

def update_candidate(
    candidate_id: int, 
    name: Optional[str] = None,
    image: Optional[str] = None,
    political_party: Optional[str] = None,
    description: Optional[str] = None
) -> Optional[Candidate]:
    """Update a candidate"""
    for i, candidate in enumerate(candidates_db):
        if candidate.id == candidate_id:
            if name is not None:
                candidate.name = name
            if image is not None:
                candidate.image = image
            if political_party is not None:
                candidate.politicalParty = political_party
            if description is not None:
                candidate.description = description
            
            candidate.updatedAt = datetime.now()
            candidates_db[i] = candidate
            return candidate
    return None

def delete_candidate(candidate_id: int) -> bool:
    """Delete a candidate"""
    for i, candidate in enumerate(candidates_db):
        if candidate.id == candidate_id:
            candidates_db.pop(i)
            return True
    return False

def search_candidates(query: str) -> List[Candidate]:
    """Search candidates by name or political party"""
    query_lower = query.lower()
    results = []
    for candidate in candidates_db:
        if (query_lower in candidate.name.lower() or 
            query_lower in candidate.politicalParty.lower() or
            query_lower in candidate.description.lower()):
            results.append(candidate)
    return results

def get_candidates_by_party(political_party: str) -> List[Candidate]:
    """Get all candidates from a specific political party"""
    return [candidate for candidate in candidates_db if candidate.politicalParty == political_party]

def get_total_count() -> int:
    """Get total number of candidates"""
    return len(candidates_db) 