from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, resumes, applications
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Allow requests from React dev server
origins = [
    "http://localhost:3000",  # React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # or use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(resumes.router)
app.include_router(applications.router)

@app.get("/")
def read_root():
    return {"message": "Job Tracker backend is live."}