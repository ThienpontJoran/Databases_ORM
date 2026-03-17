from fastapi import FastAPI
from database import start_db
from routers import species, birds, birdSpotting

app = FastAPI()


app.include_router(species.router)
app.include_router(birds.router)
app.include_router(birdSpotting.router)
start_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#