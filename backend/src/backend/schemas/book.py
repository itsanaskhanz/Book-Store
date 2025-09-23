from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    stock: int = 0


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
