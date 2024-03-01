GET List Movies: Endpoint: /manage_movies/movies/

GET View Movie Details: Endpoint: /manage_movies/movies/<movie_id>/

    Example: /manage_movies/movies/1/

POST Add Movie: Endpoint: /manage_movies/movies/

    Example Request Body: json
    {
        "title": "New Movie",
        "year": 2024,
        "directors": [{"name": "Director Name"}],
        "actors": [{"name": "Actor Name"}]
    }

GET Filter Movies by Year: Endpoint: /manage_movies/movies/?year=<year>

GET Filter Movies by Director: Endpoint: /manage_movies/movies/?directors=<director_name>

GET Filter Movies by Actor: Endpoint: /manage_movies/movies/?actors=<actor_name>

PUT Update Movie: Endpoint: /manage_movies/movies/<movie_id>/

    Example: /manage_movies/movies/1/
    Example Request Body: json
    {
        "title": "Updated Movie",
        "year": 2024,
        "directors": [{"name": "Updated Director"}],
        "actors": [{"name": "Updated Actor"}]
    }

DELETE Movie: Endpoint: /manage_movies/movies/<movie_id>/

    Example: /manage_movies/movies/1/