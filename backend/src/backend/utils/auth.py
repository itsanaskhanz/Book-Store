from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt
import os

from backend.utils.jwt_handler import validate_jwt_token  # reuse your handler

security = HTTPBearer()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"


def get_current_user(credentials=Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        email = payload.get("email")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"id": user_id, "email": email}
