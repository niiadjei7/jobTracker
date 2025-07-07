from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

#User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int 
    date_created: date = Field(default_factory=date.today)

    class config:
        orm_mode = True

#Resume schemas
class ResumeBase(BaseModel):
    file_url: str
    filename: str

class ResumeCreate(ResumeBase):
    pass

class ResumeOut(ResumeBase):
    id: int
    user_id: int
    date_uploaded: date = Field(default_factory=date.today)

    class Config:
        from_attributes = True

#Job Application Schemas
class ApplicationBase(BaseModel):
    company_name: str
    job_title: str
    job_description: str
    job_url: str
    application_date: date
    status: Optional[str] = "saved"
    notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class ApplicationOut(ApplicationBase):
    id: int
    user_id: int 
    application_date: date = Field(default_factory=date.today)

    class Config:
        from_attributes = True 


