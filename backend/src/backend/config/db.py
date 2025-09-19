import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

if not DATABASE_URL:
    raise ValueError("DB_URL is not set in .env file")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for DB


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
