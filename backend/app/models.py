from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from .database import Base
from datetime import date

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    date_created = Column(Date, default=date.today)

    job_applications = relationship("Application", back_populates="user")
    resumes = relationship("Resume", back_populates="user")

    @property
    def applied_jobs(self):
        return len(self.job_applications)

class Resume(Base):
    __tablename__= "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    file_url = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    date_uploaded = Column(Date, default=date.today)

    user = relationship("User", back_populates="resumes")

    

class Application(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    job_description = Column(Text)
    job_url = Column(String)
    application_date = Column(Date)
    status = Column(String, default="saved")
    notes = Column(Text)

    user = relationship("User", back_populates="job_applications")

class JobMatchScore(Base):
    __tablename__ = "job_match_scores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    job_id = Column(Integer, ForeignKey("job_applications.id"), index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), index=True)

    score = Column(Float, nullable=False)  
    explanation = Column(Text)            
    created_at = Column(Date, default=date.today)

    # Relationships (if needed)
    user = relationship("User")
    job = relationship("Application")
    resume = relationship("Resume")
    