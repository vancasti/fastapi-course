from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.models import Movie, MovieSchema, BearerJWT
from db.database import Session

router = APIRouter()


@router.get("/movies", tags=["movies"], dependencies=[Depends(BearerJWT())])
def get_movies():
    db = Session()
    data = db.query(Movie).all()
    return JSONResponse(content=jsonable_encoder(data))


@router.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    db = Session()
    data = db.query(Movie).filter(Movie.id == id).first()
    if data:
        return JSONResponse(content=jsonable_encoder(data))
    return JSONResponse(status_code=404, content={"message": "Film not found"})


@router.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str):
    db = Session()
    data = db.query(Movie).filter(Movie.category == category).all()
    if data:
        return JSONResponse(content=jsonable_encoder(data))
    return JSONResponse(status_code=404, content={"message": "Film not found"})


@router.post("/movies", tags=["movies"])
def create_movie(movie: MovieSchema):
    db = Session()
    new_movie = Movie(
        title=movie.title,
        overview=movie.overview,
        year=movie.year,
        rating=movie.rating,
        category=movie.category,
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return JSONResponse(
        status_code=201, content={"message": "Successfully added a new film"}
    )


@router.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: MovieSchema):
    db = Session()
    data = db.query(Movie).filter(Movie.id == id).first()
    if data:
        data.title = movie.title
        data.overview = movie.overview
        data.year = movie.year
        data.rating = movie.rating
        data.category = movie.category
        db.commit()
        return JSONResponse(content={"message": "Successfully updated a film"})
    return JSONResponse(status_code=404, content={"message": "Film not found"})


@router.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
    db = Session()
    data = db.query(Movie).filter(Movie.id == id).first()
    if data:
        db.delete(data)
        db.commit()
        return JSONResponse(content={"message": "Successfully deleted a film"})
    return JSONResponse(status_code=404, content={"message": "Film not found"})
