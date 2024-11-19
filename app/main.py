from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from db.database import engine, Base
from app.routers import movie
from app.routers import user

app = FastAPI(
    title="fastapi-course",
    description="Building an API with FastAPI",
    version="1.0.0",
)

app.include_router(movie.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["root"])
def root():
    return HTMLResponse("<h2>Hola Mundo</h2>")
