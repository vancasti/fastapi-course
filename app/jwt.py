import jwt
import os


def create_token(data: dict):
    # replace by env variable
    return jwt.encode(payload=data, key=str(os.getenv("SECRET_KEY")), algorithm="HS256")
