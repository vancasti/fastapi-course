from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from .models import Movie, User
from .jwt import create_token


app = FastAPI(
    title="fastapi-course",
    description="Building an API with FastAPI",
    version="1.0.0",
)

movies = [
    {
        "id": 1,
        "title": "El Padrino",
        "overview": "El Padrino talala.....",
        "year": 1972,
        "rating": 9.2,
        "category": "Crimen",
    }
]


@app.get("/", tags=["root"])
def root():
    return HTMLResponse("<h2>Hola Mundo</h2>")


@app.post("/login", tags=["auth"])
def login(user: User):
    token : str = create_token(user.dict())
    print(token)
    return user


@app.get("/movies", tags=["movies"])
def get_movies():
    return JSONResponse(content=movies)


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    # by interate on list
    for movie in movies:
        if movie.get("id") == id:
            return [movie]
    # by list comprehesion
    # newlist = [x for x in fruits if "a" in x]
    return [movie for movie in movies if movie.get("id") == id]


@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str):
    return [movie for movie in movies if movie.get("category") == category]


@app.post("/movies", tags=["movies"])
def create_movie(movie: Movie):
    print(Body)
    movies.append(movie)
    return JSONResponse(
        status_code=201, content={"message": "Successfully added a new film"}
    )


@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    for movie in movies:
        if movie.get("id") == id:
            movie["title"] = movie.title
            movie["overview"] = movie.overview
            movie["year"] = movie.year
            movie["rating"] = movie.rating
            movie["category"] = movie.category
            return movies


@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
    for item in movies:
        if item.get("id") == id:
            movies.remove(item)
            return JSONResponse(
                status_code=204,
                content={"message": "Successfully deleted an existing film"},
            )
