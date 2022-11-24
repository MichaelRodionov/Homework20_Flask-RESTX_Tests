from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.models import MovieSchema
from helpers import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    @auth_required
    def get():
        """This view returns all movies by pages or sort movies by director/genre/year by GET request"""
        return movies_schema.dump(movie_service.get_movies()), 200

    @staticmethod
    @admin_required
    def post():
        """This view is needed to add a new movie by POST request"""
        data = request.json
        serialized_data = movie_schema.load(data)
        new_movie = movie_service.add_movie(serialized_data)
        return "", 201, {"Location": f"/movies/{new_movie.id}"}


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @staticmethod
    @auth_required
    def get(movie_id):
        """This view return one movie filtered by movie_id by GET request"""
        movie = movie_service.get_one_movie(movie_id)
        if not movie:
            return 'movie not found', 404
        return movie_schema.dump(movie), 200

    @staticmethod
    @admin_required
    def put(movie_id):
        """This view is needed to update movie filtered by movie_id by PUT request"""
        data = request.json
        data['id'] = movie_id
        return movie_service.update_movie_full(data), 204

    @staticmethod
    @admin_required
    def delete(movie_id):
        """This view is needed to delete movie filtered by movie_id by DELETE request"""
        return movie_service.delete_one_movie(movie_id)
