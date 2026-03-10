from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from models.birds import Bird, BirdCreate
from repositories.birds import BirdRepository
from database import get_session

router = APIRouter(prefix="/birds", tags=["Birds"])

def get_bird_repo(session: Annotated[Session, Depends(get_session)]) -> BirdRepository:
    return BirdRepository(session)

@router.get("/", response_model=List[Bird])
async def get_birds(repo: Annotated[BirdRepository, Depends(get_bird_repo)]):
    return repo.get_all()

@router.post("/", response_model=Bird)
async def add_bird(bird: BirdCreate, repo: Annotated[BirdRepository, Depends(get_bird_repo)]):
    try:
        return repo.insert(bird)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))