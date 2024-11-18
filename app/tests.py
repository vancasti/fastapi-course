import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


@pytest.fixture
def movie_data():
    return {
        "title": "Inception",
        "overview": "A skilled thief is given a chance at redemption if he can successfully perform inception.",
        "year": 2010,
        "rating": 8.8,
        "category": "Science Fiction",
    }


def test_create_movie_success(movie_data):
    response = client.post("/movies", json=movie_data)
    assert response.status_code == 201, response.text
    assert response.json() == {"message": "Successfully added a new film"}
