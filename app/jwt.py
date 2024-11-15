import jwt
import os


def create_token(data: dict):
    return jwt.encode(payload=data, key=str(os.getenv("SECRET_KEY")), algorithm="HS256")


def validate_token(token: str):
    return jwt.decode(token, key=str(os.getenv("SECRET_KEY")), algorithms=["HS256"])