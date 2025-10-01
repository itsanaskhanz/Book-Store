from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.models.user import User
from backend.schemas.user import UserCreate, LoginRequest
from backend.utils.password_hasing import hash_pwd, validate_pwd
from backend.utils.jwt_handler import get_jwt_token


def signup_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_pwd(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password.decode("utf-8"),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(request: LoginRequest, db: Session):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not validate_pwd(request.password, user.hashed_password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = get_jwt_token({"user_id": user.id, "email": user.email})
    return {"access_token": token, "token_type": "bearer"}


def get_users(db: Session):
    return db.query(User).all()


def update_user(user_id: int, updated_data: dict, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updated_data.items():
        if key != "id":
            setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": f"User with ID {user_id} deleted successfully"}
