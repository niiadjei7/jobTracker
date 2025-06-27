from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

#app.include_router(jobs.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Job Tracker backend is live."}