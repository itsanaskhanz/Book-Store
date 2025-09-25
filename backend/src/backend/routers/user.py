from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.user import UserCreate, UserRead
from backend.services.user_service import (
    create_user_service,
    get_user_service,
    get_all_users_service,
    update_user_service,
    delete_user_service
)
from backend.config.db import get_db

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_service(user_id, db)


@router.get("/", response_model=List[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    return get_all_users_service(db)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, updated_data: UserCreate, db: Session = Depends(get_db)):
    return update_user_service(user_id, updated_data.dict(exclude_unset=True), db)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(user_id, db)
