from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.models.book import Book
from backend.models.user import User
from backend.schemas.book import BookCreate


def create_book(book: BookCreate, user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_book = Book(
        title=book.title,
        author=book.author,
        price=book.price,
        stock=book.stock,
        user_id=user_id
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def get_books(db: Session):
    return db.query(Book).all()


def update_book(book_id: int, updated_data: dict, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in updated_data.items():
        if key != "id":
            setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"detail": f"Book with ID {book_id} deleted successfully"}
