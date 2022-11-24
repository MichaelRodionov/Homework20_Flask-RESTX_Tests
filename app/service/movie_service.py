from sqlalchemy.orm.exc import UnmappedInstanceError

from app.dao import MovieDAO
from app.dao.models.models import Movie


class MovieService:
    """
    Service is needed to work with movies views and MovieDAO
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list:
        return self.movie_dao.get_all_movies()

    def add_movie(self, data):
        """
        This
        :return:
        """
        movie_data = Movie(**data)
        return self.movie_dao.add_new_movie(movie_data)

    def get_one_movie(self, movie_id: int):
        return self.movie_dao.get_movie_by_id(movie_id)

    def update_movie_full(self, data):
        movie_to_update = self.get_one_movie(data['id'])
        movie_to_update.title = data.get('title')
        movie_to_update.description = data.get('description')
        movie_to_update.trailer = data.get('trailer')
        movie_to_update.year = data.get('year')
        movie_to_update.rating = data.get('rating')
        return self.movie_dao.edit_movie(movie_to_update)

    def delete_one_movie(self, movie_id: int):
        try:
            return self.movie_dao.delete_movie(movie_id), 204
        except UnmappedInstanceError:
            return "nothing to delete"
