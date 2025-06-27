from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


