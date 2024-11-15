from pydantic import BaseModel, Field
from typing import List, Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str = Field(min_length=3)
    year: int
    rating: float
    category: str


class User(BaseModel):
    email: str
    password: str