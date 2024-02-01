from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..hashing import verify
from .. import database, schemas, models, JWTToken

router = APIRouter(tags=["Authentication"], prefix="/login")


@router.post("/")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials",
        )
    if not verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials",
        )

    # JWT Token Creation

    access_token = JWTToken.create_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
