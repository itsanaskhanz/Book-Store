import bcrypt


def hash_pwd(password: str) -> bytes:
    byte_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password


def validate_pwd(plain_password: str, hash_password: bytes) -> bool:
    plain_password_bytes = plain_password.encode("utf-8")
    return bcrypt.checkpw(plain_password_bytes, hash_password)
