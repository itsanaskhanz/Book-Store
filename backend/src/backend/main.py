import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import book, user

load_dotenv()

app = FastAPI(title="Book-Store API")

origins = os.getenv("CORS_ORIGIN", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router, prefix="/api/book", tags=["Books"])
app.include_router(user.router, prefix="/api/auth", tags=["Users"])


@app.get("/")
def greeting():
    return "Welcome to the Book-Store API"
