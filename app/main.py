from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from . import crud
from .schemas import CandidateCreate, CandidateUpdate, CandidateResponse, CandidateListResponse

app = FastAPI(
    title="Political Candidates API",
    description="A FastAPI backend for managing political candidates",
    version="1.0.0"
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev server and Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Political Candidates API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is operational"}

@app.get("/api/candidates", response_model=CandidateListResponse)
async def get_candidates(
    skip: int = Query(0, ge=0, description="Number of candidates to skip"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of candidates to return"),
    search: Optional[str] = Query(None, description="Search query for candidates")
):
    """Get all candidates with optional search and pagination"""
    if search:
        candidates = crud.search_candidates(search)
        return CandidateListResponse(
            candidates=candidates,
            total=len(candidates),
            page=skip // limit + 1,
            size=limit
        )
    else:
        candidates = crud.get_candidates(skip=skip, limit=limit)
        total = crud.get_total_count()
        return CandidateListResponse(
            candidates=candidates,
            total=total,
            page=skip // limit + 1,
            size=limit
        )

@app.get("/api/candidates/{candidate_id}", response_model=CandidateResponse)
async def get_candidate(candidate_id: int):
    """Get a specific candidate by ID"""
    candidate = crud.get_candidate(candidate_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return candidate

@app.post("/api/candidates", response_model=CandidateResponse, status_code=201)
async def create_candidate(candidate: CandidateCreate):
    """Create a new candidate"""
    new_candidate = crud.create_candidate(
        name=candidate.name,
        image=candidate.image,
        political_party=candidate.politicalParty,
        description=candidate.description
    )
    return new_candidate

@app.put("/api/candidates/{candidate_id}", response_model=CandidateResponse)
async def update_candidate(candidate_id: int, candidate_update: CandidateUpdate):
    """Update an existing candidate"""
    updated_candidate = crud.update_candidate(
        candidate_id=candidate_id,
        name=candidate_update.name,
        image=candidate_update.image,
        political_party=candidate_update.politicalParty,
        description=candidate_update.description
    )
    if updated_candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return updated_candidate

@app.patch("/api/candidates/{candidate_id}", response_model=CandidateResponse)
async def partial_update_candidate(candidate_id: int, candidate_update: CandidateUpdate):
    """Partially update an existing candidate"""
    updated_candidate = crud.update_candidate(
        candidate_id=candidate_id,
        name=candidate_update.name,
        image=candidate_update.image,
        political_party=candidate_update.politicalParty,
        description=candidate_update.description
    )
    if updated_candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return updated_candidate

@app.delete("/api/candidates/{candidate_id}")
async def delete_candidate(candidate_id: int):
    """Delete a candidate"""
    success = crud.delete_candidate(candidate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"message": "Candidate deleted successfully"}

@app.get("/api/candidates/party/{political_party}", response_model=List[CandidateResponse])
async def get_candidates_by_party(political_party: str):
    """Get all candidates from a specific political party"""
    candidates = crud.get_candidates_by_party(political_party)
    return candidates

@app.get("/api/candidates/search", response_model=List[CandidateResponse])
async def search_candidates(query: str = Query(..., description="Search query")):
    """Search candidates by name, party, or description"""
    candidates = crud.search_candidates(query)
    return candidates

@app.get("/api/stats")
async def get_stats():
    """Get basic statistics about candidates"""
    total_candidates = crud.get_total_count()
    all_candidates = crud.get_candidates()
    
    # Count candidates by party
    party_counts = {}
    for candidate in all_candidates:
        party = candidate.political_party
        party_counts[party] = party_counts.get(party, 0) + 1
    
    return {
        "total_candidates": total_candidates,
        "parties": party_counts,
        "unique_parties": len(party_counts)
    } 