from pydantic import BaseModel, EmailStr, Field
from datetime import date

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int 
    date_created: date = Field(default_factory=date.today)

    class config:
        orm_mode = True

