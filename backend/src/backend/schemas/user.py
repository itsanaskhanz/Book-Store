from pydantic import BaseModel
from typing import List
from backend.schemas.book import BookRead


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    books: List[BookRead] = []

    class Config:
        from_attributes = True
