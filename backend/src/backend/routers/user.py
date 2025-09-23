from fastapi import APIRouter

router = APIRouter(tags=["Users"])


@router.post("/")
def create_user():
    return "User created successfully"


@router.get("/{user_id}")
def get_user(user_id: int):
    return f"User details for ID {user_id}"


@router.put("/{user_id}")
def update_user(user_id: int):
    return f"User with ID {user_id} updated successfully"


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return f"User with ID {user_id} deleted successfully"


@router.get("/")
def get_all_users():
    return "List of all users"
