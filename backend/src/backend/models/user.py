from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

    # relationship with Book
    books = relationship("Book", back_populates="owner",
                         cascade="all, delete-orphan")
