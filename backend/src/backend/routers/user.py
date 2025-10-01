from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.user import UserCreate, UserRead, LoginRequest
from backend.services.user_service import signup_user, login_user, get_users, update_user, delete_user
from backend.config.db import get_db
from backend.utils.auth import get_current_user

router = APIRouter()


@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return signup_user(user, db)


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return login_user(request, db)


@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.put("/{user_id}", response_model=UserRead)
def update(
    user_id: int,
    updated_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if current_user["id"] != user_id:
        raise HTTPException(
            status_code=403, detail="Not allowed to update this account")
    return update_user(user_id, updated_data.dict(exclude_unset=True), db)


@router.delete("/{user_id}")
def delete(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if current_user["id"] != user_id:
        raise HTTPException(
            status_code=403, detail="Not allowed to delete this account")
    return delete_user(user_id, db)
