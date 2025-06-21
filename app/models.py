from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class Candidate(BaseModel):
    id: int
    name: str
    image: str
    politicalParty: str
    description: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    
    def __repr__(self):
        return f"<Candidate(id={self.id}, name='{self.name}', party='{self.politicalParty}')>" 