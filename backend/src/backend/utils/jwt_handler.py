import os
from dotenv import load_dotenv
import jwt
import datetime
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in .env file")


def get_jwt_token(payload: dict, expires_in: int = 3600) -> str:
    payload_copy = payload.copy()
    payload_copy["exp"] = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(seconds=expires_in)
    token = jwt.encode(payload_copy, SECRET_KEY, algorithm="HS256")
    return token


def validate_jwt_token(token: str) -> dict | None:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        print("Token expired!")
    except jwt.InvalidTokenError:
        print("Invalid token!")
    return None
