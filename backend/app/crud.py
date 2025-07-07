from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from datetime import date

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#---USER CRUD LOGIC---
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_data: schemas.UserCreate):
    hashed_pw = pwd_context.hash(user_data.password)

    db_user = models.User(
        email=user_data.email,
        password_hash=hashed_pw
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Return the fully loaded user

    return db_user

#---RESUME CRUD LOGIC---
def create_resume(db: Session, resume: schemas.ResumeCreate, user_id: int) -> models.Resume:
    db_resume = models.Resume(
        file_url=resume.file_url,
        filename=resume.filename,
        user_id=user_id,
        date_uploaded=date.today()
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def get_all_resumes(db: Session, user_id: int):
    return db.query(models.Resume).filter(models.Resume.user_id==user_id).all()

def get_resume(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()

#--APPLICATION CRUD LOGIC--
def create_application(db: Session, application: schemas.ApplicationCreate, user_id: int) -> models.Application:
    db_application = models.Application(
        company_name = application.company_name,
        job_title = application.job_title,
        job_description = application.job_description,
        job_url = application.job_url,
        status = application.status,
        notes = application.notes,
        user_id = user_id,
        application_date = date.today()
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

def get_all_applications(db: Session, user_id: int):
    return db.querry(models.Application).filter(models.Applicaiton.user_id==user_id).all()

def get_application(db: Session, application_id: int):
    return db.querry(models.Application).filter(models.Application.id == application_id).first()

