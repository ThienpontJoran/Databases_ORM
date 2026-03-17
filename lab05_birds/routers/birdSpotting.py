from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.birdSpotting import Birdspotting, BirdspottingCreate
from repositories.birdSpotting import BirdspottingRepository

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])

def get_repo(session: Annotated[Session, Depends(get_session)]):
    return BirdspottingRepository(session)


@router.get("/", response_model=List[Birdspotting])
async def get_all(repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    return repo.get_all()


@router.get("/{id}", response_model=Birdspotting)
async def get_one(id: int, repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    observation = repo.get_one(id)

    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")

    return observation


@router.post("/", response_model=Birdspotting)
async def create(
    observation: BirdspottingCreate,
    repo: Annotated[BirdspottingRepository, Depends(get_repo)],
):
    try:
        return repo.insert(observation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))