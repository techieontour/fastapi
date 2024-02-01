from fastapi import APIRouter, Depends, status
from typing import List
from .. import database, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(tags=["Blogs"], prefix="/blog")
database = get_db


# GETALL Method
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ShowBlog],
)
def all(db: Session = Depends(database)):
    return blog.get_all(db)


# POST Method
@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create(request: schemas.Blog, db: Session = Depends(database)):
    return blog.create(request, db)


# DELETE Method
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database)):
    return blog.delete(id, db)


# UPDATE Method
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database)):
    return blog.update(id, request, db)


# GETBYID Method
@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
def show(id, db: Session = Depends(database)):
    return blog.show(id, db)
