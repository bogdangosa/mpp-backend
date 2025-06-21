from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class CandidateBase(BaseModel):
    name: str
    image: str
    politicalParty: str
    description: str

class CandidateCreate(CandidateBase):
    pass

class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    politicalParty: Optional[str] = None
    description: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class CandidateListResponse(BaseModel):
    candidates: list[CandidateResponse]
    total: int
    page: int
    size: int 