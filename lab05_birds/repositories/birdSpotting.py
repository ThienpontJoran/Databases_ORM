from sqlmodel import Session, select
from models.birdSpotting import Birdspotting, BirdspottingCreate
from models.birds import Bird

class BirdspottingRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Birdspotting)
        return self.session.exec(statement).all()

    def get_one(self, id: int):
        return self.session.get(Birdspotting, id)

    def insert(self, payload: BirdspottingCreate):

        # check if bird exists
        bird = self.session.get(Bird, payload.bird_id)
        if not bird:
            raise ValueError("Bird does not exist")

        observation = Birdspotting(**payload.dict())

        self.session.add(observation)
        self.session.commit()
        self.session.refresh(observation)

        return observation