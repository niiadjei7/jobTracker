from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post("/", response_model=schemas.ApplicationOut)
def log_application(
    application: schemas.ApplicationCreate,
    user_id: int,
    db: Session=Depends(database.get_db)
):
    return crud.create_application(db=db, application=application, user_id=user_id)

@router.get("/{user_id}" , response_model=list[schemas.ApplicationOut])
def get_applications(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_all_applications(db=db, user_id=user_id)

@router.get("/details/{application_id}", response_model=schemas.ApplicationOut)
def get_application_by_id(application_id: int, db: Session = Depends(database.get_db)):
    application = crud.get_application(db=db, application_id=application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application