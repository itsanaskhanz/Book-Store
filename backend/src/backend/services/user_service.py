from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.models.user import User
from backend.schemas.user import UserCreate, UserRead


def create_user_service(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_service(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_all_users_service(db: Session):
    return db.query(User).all()


def update_user_service(user_id: int, updated_data: dict, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in updated_data.items():
        if key != "id":
            setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user_service(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": f"User with ID {user_id} deleted successfully"}
