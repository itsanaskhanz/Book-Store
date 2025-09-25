from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.book import BookCreate, BookRead
from backend.services.book_service import (
    create_book_service,
    get_book_service,
    get_all_books_service,
    update_book_service,
    delete_book_service
)
from backend.config.db import get_db

router = APIRouter()


@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, user_id: int, db: Session = Depends(get_db)):
    return create_book_service(book, user_id, db)


@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return get_book_service(book_id, db)


@router.get("/", response_model=List[BookRead])
def get_all_books(db: Session = Depends(get_db)):
    return get_all_books_service(db)


@router.put("/{book_id}", response_model=BookRead)
def update_book(book_id: int, updated_data: BookCreate, db: Session = Depends(get_db)):
    return update_book_service(book_id, updated_data.dict(exclude_unset=True), db)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return delete_book_service(book_id, db)
