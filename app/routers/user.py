from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import UserSchema
from app.jwt import create_token

router = APIRouter()


@router.post("/login", tags=["auth"])
def login(user: UserSchema):
    token: str = create_token(user.dict())
    return JSONResponse(content=token)
