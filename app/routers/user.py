from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils.hash_utils import hash_password, verify_password
from app.auth2 import get_current_user


router = APIRouter(prefix="/users", tags=["Users"])

# ✅ REGISTER
@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ✅ CURRENT USER (/users/me)
@router.get("/me", response_model=schemas.UserOut)
def get_me(current_user: schemas.UserOut = Depends(get_current_user)):
    return current_user
