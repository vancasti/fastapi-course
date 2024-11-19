from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from .models import UserSchema
from .jwt import create_token
from db.database import engine, Base
from app.routers import movie

app = FastAPI(
    title="fastapi-course",
    description="Building an API with FastAPI",
    version="1.0.0",
)

app.include_router(movie.router)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["root"])
def root():
    return HTMLResponse("<h2>Hola Mundo</h2>")


@app.post("/login", tags=["auth"])
def login(user: UserSchema):
    token: str = create_token(user.dict())
    return JSONResponse(content=token)
