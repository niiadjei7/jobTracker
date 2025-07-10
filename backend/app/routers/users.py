from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db=db, user_data=user)

@router.post("/login", response_model=schemas.UserResponse)
def login(user_data: schemas.UserLogin, db: Session = Depends(database.get_db)):
    print(user_data)
    user = crud.get_user_by_email(db, user_data.email)
    if not user or not crud.pwd_context.verify(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return user