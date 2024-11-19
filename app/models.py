from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from fastapi.security import HTTPBearer
from db.database import Base


class BearerJWT(HTTPBearer): ...


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)


class MovieSchema(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    email: str
    password: str
