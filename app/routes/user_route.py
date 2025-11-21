from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse
from typing import List


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return UserService.list_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, data)

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    user = UserService.update_user(db, user_id, data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

