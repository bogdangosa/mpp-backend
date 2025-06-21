from typing import List, Optional
from datetime import datetime
from .models import Candidate

# In-memory storage for candidates
candidates_db: List[Candidate] = []

# Initialize with some sample data
def initialize_sample_data():
    sample_candidates = [
        Candidate(
            id=1,
            name="Sarah Johnson",
            image="https://images.unsplash.com/photo-1494790108755-2616b612b786?w=400&h=400&fit=crop&crop=face",
            politicalParty="Progressive Democrats",
            description="Sarah Johnson is a dedicated public servant with over 15 years of experience in local government. She focuses on education reform, healthcare accessibility, and environmental protection.",
            createdAt=datetime.now(),
            updatedAt=None
        ),
        Candidate(
            id=2,
            name="Michael Chen",
            image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face",
            politicalParty="Conservative Alliance",
            description="Michael Chen brings a business perspective to politics, having served as CEO of a successful technology company. He advocates for fiscal responsibility, deregulation, and strong national security.",
            createdAt=datetime.now(),
            updatedAt=None
        ),
        Candidate(
            id=3,
            name="Maria Rodriguez",
            image="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=face",
            politicalParty="Green Future Party",
            description="Maria Rodriguez is an environmental scientist and activist who has dedicated her career to fighting climate change. She promotes renewable energy, sustainable development, and social justice.",
            createdAt=datetime.now(),
            updatedAt=None
        ),
        Candidate(
            id=4,
            name="David Thompson",
            image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face",
            politicalParty="Independent Coalition",
            description="David Thompson is a retired military officer who believes in bipartisan solutions to complex problems. He emphasizes national unity, infrastructure development, and support for veterans.",
            createdAt=datetime.now(),
            updatedAt=None
        ),
        Candidate(
            id=5,
            name="Lisa Park",
            image="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=face",
            politicalParty="Liberal Reform Party",
            description="Lisa Park is a civil rights attorney who has fought for equality and justice throughout her career. She champions criminal justice reform, voting rights, and economic opportunity for all.",
            createdAt=datetime.now(),
            updatedAt=None
        ),
        Candidate(
            id=6,
            name="Robert Williams",
            image="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=face",
            politicalParty="Traditional Values Party",
            description="Robert Williams is a community leader and small business owner who values traditional American principles. He focuses on family values, religious freedom, and local control of government.",
            createdAt=datetime.now(),
            updatedAt=None
        )
    ]
    
    candidates_db.extend(sample_candidates)

# Initialize sample data when module is imported
initialize_sample_data()

def get_next_id() -> int:
    """Get the next available ID for a new candidate"""
    if not candidates_db:
        return 1
    return max(candidate.id for candidate in candidates_db) + 1 