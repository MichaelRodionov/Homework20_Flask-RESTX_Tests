import pytest

from app.service.movie_service import MovieService
from tests.conftest.conftest import movie_dao


# ----------------------------------------------------------------
# test class of movie service
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao: movie_dao):
        """
        Create an object of MovieService
        :param movie_dao:
        """
        self.movie_service = MovieService(movie_dao)

    def test_get_all_movies(self):
        movies = self.movie_service.get_movies()
        assert movies is not None, 'Error: no response from database'
        assert len(movies) > 1, 'Error: empty list of movies'

    def test_get_movie_by_id(self):
        movie = self.movie_service.get_one_movie(1)
        assert movie is not None, 'Error: movie not found'
        assert movie.id is not None, 'Error: movie not found'
        assert type(movie.id) is int, 'Error: wrong type'

    def test_add_new_movie(self):
        new_movie_data = {
            "title": "test_movie_4",
            "description": "test_description_movie_4",
            "trailer": "https://www.youtube.com/test_movie_4",
            "year": 2019,
            "rating": 8.0,
            "genre_id": 20,
            "director_id": 2,
            "id": 4
        }
        new_movie = self.movie_service.add_movie(new_movie_data)
        assert new_movie.id is not None, 'Error: movie not created'
        assert new_movie.id == new_movie_data.get('id'), 'Error: wrong id'
        assert type(new_movie.id) is int, 'Error: wrong type'

    def test_edit_movie(self):
        movie_data = {
            'id': 1,
            'title': 'test_title_edit_movie',
            'year': 2023
        }
        self.movie_service.update_movie_full(movie_data)

    def test_delete_movie(self):
        self.movie_service.delete_one_movie(1)
