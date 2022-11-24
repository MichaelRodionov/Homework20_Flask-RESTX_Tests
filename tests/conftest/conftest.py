import pytest
from unittest.mock import MagicMock

from app.dao.MovieDAO import MovieDAO
from app.dao.GenreDAO import GenreDAO
from app.dao.DirectorDAO import DirectorDAO
from tests.conftest.test_data import ALL_MOVIES, MOVIE_BY_ID, ADD_NEW_MOVIE, ALL_DIRECTORS, DIRECTOR_BY_ID, \
    ALL_GENRES, GENRE_BY_ID


# ----------------------------------------------------------------
# create fixture to mock MovieDAO methods
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_dao.get_all_movies = MagicMock(return_value=ALL_MOVIES)
    movie_dao.get_movie_by_id = MagicMock(return_value=MOVIE_BY_ID)
    movie_dao.add_new_movie = MagicMock(return_value=ADD_NEW_MOVIE)
    movie_dao.edit_movie = MagicMock()
    movie_dao.delete_movie = MagicMock()
    return movie_dao


# ----------------------------------------------------------------
# create fixture to mock DirectorDAO methods
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_dao.get_all_directors = MagicMock(return_value=ALL_DIRECTORS)
    director_dao.get_director_by_id = MagicMock(return_value=DIRECTOR_BY_ID)
    director_dao.add_new_director_or_update = MagicMock()
    director_dao.delete_director = MagicMock()
    return director_dao


# ----------------------------------------------------------------
# create fixture to mock GenreDAO methods
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_dao.get_all_genres = MagicMock(return_value=ALL_GENRES)
    genre_dao.get_genre_by_id = MagicMock(return_value=GENRE_BY_ID)
    genre_dao.add_genre_or_update = MagicMock()
    genre_dao.delete_genre = MagicMock()
    return genre_dao
