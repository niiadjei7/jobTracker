from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, resumes, applications



app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(resumes.router)
app.include_router(applications.router)

@app.get("/")
def read_root():
    return {"message": "Job Tracker backend is live."}