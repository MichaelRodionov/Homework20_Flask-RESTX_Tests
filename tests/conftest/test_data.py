from app.dao.models.models import Movie, Genre, Director


# ----------------------------------------------------------------
# Movies data
ALL_MOVIES = [
    Movie(
        id=1,
        title='test_film_1',
        description='test_description_1',
        trailer='https://www.youtube.com/test_film_1',
        year=1996,
        rating='9.0',
        genre_id=1,
        director_id=2
    ),
    Movie(
        id=2,
        title='test_film_2',
        description='test_description_2',
        trailer='https://www.youtube.com/test_film_2',
        year=1997,
        rating='8.0',
        genre_id=2,
        director_id=3
    ),
    Movie(
        id=3,
        title='test_film_3',
        description='test_description_3',
        trailer='https://www.youtube.com/test_film_3',
        year=1998,
        rating='7.0',
        genre_id=3,
        director_id=4
    )
]

MOVIE_BY_ID = Movie(
    id=1,
    title='test_film_1',
    description='test_description_1',
    trailer='https://www.youtube.com/test_film_1',
    year=1996,
    rating='9.0',
    genre_id=1,
    director_id=2
)

ADD_NEW_MOVIE = Movie(id=4)
# ----------------------------------------------------------------
# Genres data
ALL_GENRES = [
    Genre(
        id=1,
        name='test_genre_1'
    ),
    Genre(
        id=2,
        name='test_genre_2'
    ),
    Genre(
        id=3,
        name='test_genre_3'
    ),
]

GENRE_BY_ID = Genre(
    id=1,
    name='test_genre_1'
)
# ----------------------------------------------------------------
# Directors data
ALL_DIRECTORS = [
    Director(
        id=1,
        name='test_director_1'
    ),
    Director(
        id=2,
        name='test_director_2'
    ),
    Director(
        id=3,
        name='test_director_3'
    )
]

DIRECTOR_BY_ID = Director(
    id=1,
    name='test_director_1'
)
