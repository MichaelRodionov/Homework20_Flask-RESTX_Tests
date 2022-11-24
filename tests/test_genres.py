import pytest

from app.service.genre_service import GenreService
from tests.conftest.conftest import genre_dao


# ----------------------------------------------------------------
# test class of genre service
class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao: genre_dao):
        """
        Create an object of GenreService
        :param genre_dao:
        """
        self.genre_service = GenreService(genre_dao)

    def test_get_genres(self):
        genres = self.genre_service.get_genres()
        assert genres is not None, 'Error: no response from database'
        assert len(genres) > 1, 'Error: empty list of directors'

    def test_get_genre(self):
        genre = self.genre_service.get_genre(1)
        assert genre is not None, 'Error: genre not found'
        assert genre.id is not None, 'Error: genre not found'
        assert type(genre.id) is int, 'Error: wrong type'

    def test_add_genre(self):
        new_genre_data = {
            "id": 4,
            "name": "test_genre_4",
        }
        new_genre = self.genre_service.add_genre(new_genre_data)
        assert new_genre.id is not None, 'Error: genre not created'

    def test_update_genre(self):
        genre_data = {
            "id": 1,
            "name": "test_update"
        }
        self.genre_service.update_genre(genre_data)

    def test_delete_genre(self):
        self.genre_service.delete_genre(1)
