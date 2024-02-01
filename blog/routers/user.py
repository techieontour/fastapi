from fastapi import APIRouter, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(tags=["Users"], prefix="/user")
database = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database)):
    return user.get_user(id, db)
