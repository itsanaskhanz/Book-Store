from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.book import BookCreate, BookRead
from backend.services.book_service import (
    create_book,
    get_book,
    get_books,
    update_book,
    delete_book,
)
from backend.config.db import get_db
from backend.utils.auth import get_current_user

router = APIRouter()


@router.post("/", response_model=BookRead)
def create(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 👈 get user from token
):
    return create_book(book, current_user["id"], db)


@router.get("/{book_id}", response_model=BookRead)
def read(book_id: int, db: Session = Depends(get_db)):
    return get_book(book_id, db)


@router.get("/", response_model=List[BookRead])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)


@router.put("/{book_id}", response_model=BookRead)
def update(
    book_id: int,
    updated_data: BookCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 👈 require token
):
    return update_book(book_id, updated_data.dict(exclude_unset=True), db)


@router.delete("/{book_id}")
def delete(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # 👈 require token
):
    return delete_book(book_id, db)
