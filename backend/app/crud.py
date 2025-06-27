from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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