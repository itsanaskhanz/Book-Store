from fastapi import APIRouter

router = APIRouter(tags=["Books"])


@router.post("/")
def create_book():
    return "Book created successfully"


@router.get("/{book_id}")
def get_book(book_id: int):
    return f"Details of book with ID {book_id}"


@router.put("/{book_id}")
def update_book(book_id: int):
    return f"Book with ID {book_id} updated successfully"


@router.delete("/{book_id}")
def delete_book(book_id: int):
    return f"Book with ID {book_id} deleted successfully"


@router.get("/")
def get_all_books():
    return "List of all books"
