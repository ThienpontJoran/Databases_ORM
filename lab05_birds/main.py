from fastapi import FastAPI
from database import start_db, get_session
from routers.species import router as species_router

app = FastAPI()
app.include_router(species_router)
start_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}

