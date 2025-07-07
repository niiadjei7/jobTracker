from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models
import shutil
import os
from datetime import datetime


router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)

UPLOAD_DIR = 'uploaded_resume'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=schemas.ResumeOut)
async def upload_resume(
    file: UploadFile = File(...),
    filename: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(database.get_db)
):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    saved_filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, saved_filename)

    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Build file_url (if serving later)
    file_url = f"/{UPLOAD_DIR}/{saved_filename}"  # for now just a relative path

    # Create DB entry
    resume_data = schemas.ResumeCreate(file_url=file_url, filename=filename)
    return crud.create_resume(db=db, resume=resume_data, user_id=user_id)

@router.get("/{user_id}", response_model=list[schemas.ResumeOut])
def get_resumes(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_all_resumes(db=db, user_id=user_id)

@router.get("/details/{resume_id}", response_model=schemas.ResumeOut)
def get_resume_by_id(resume_id: int, db: Session = Depends(database.get_db)):
    resume = crud.get_resume(db=db, resume_id=resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume
   