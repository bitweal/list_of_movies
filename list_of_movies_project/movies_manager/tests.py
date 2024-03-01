from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import MovieViewSet
from .models import Movie, Director, Actor
from .serializers import MovieSerializer


class MovieAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.movie_view = MovieViewSet.as_view({'get': 'list', 'post': 'create'})
        self.detail_view = MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
        self.director = Director.objects.create(name='Existing Director')
        self.actor = Actor.objects.create(name='Existing Actor')
        self.movie = Movie.objects.create(title='Existing Movie', year=2023)
        self.movie.directors.add(self.director)
        self.movie.actors.add(self.actor)
        self.movie_data = {
            'title': 'Test Movie',
            'year': 2024,
            'directors': [{'name': 'Test Director'}],
            'actors': [{'name': 'Test Actor'}]
        }

    def test_create_movie(self):
        request = self.factory.post('/manage_movies/movies/', self.movie_data, format='json')
        response = self.movie_view(request)
        self.assertEqual(response.status_code, 201)

    def test_list_movies(self):
        request = self.factory.get('/manage_movies/movies/')
        response = self.movie_view(request)
        self.assertEqual(response.status_code, 200)

    def test_movie_filter_year(self):
        request = self.factory.get('/manage_movies/movies/?year=2023')
        response = self.movie_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

    def test_movie_filter_directors(self):
        request = self.factory.get('/manage_movies/movies/?directors=Existing Director')
        response = self.movie_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

    def test_movie_filter_actors(self):
        request = self.factory.get('/manage_movies/movies/?actors=Existing Actor')
        response = self.movie_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

    def test_retrieve_movie(self):
        request = self.factory.get('/manage_movies/movies/{}/'.format(self.movie.id))
        response = self.detail_view(request, pk=self.movie.id)
        self.assertEqual(response.status_code, 200)

    def test_update_movie(self):
        update_data = {
            'title': 'Updated Movie',
            'year': 2024,
            'directors': [{'name': 'Test Director'}],
            'actors': [{'name': 'Test Actor'}]
        }
        request = self.factory.put('/manage_movies/movies/{}/'.format(self.movie.id), update_data, format='json')
        response = self.detail_view(request, pk=self.movie.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Movie')

    def test_delete_movie(self):
        request = self.factory.delete('/manage_movies/movies/{}/'.format(self.movie.id))
        response = self.detail_view(request, pk=self.movie.id)
        self.assertEqual(response.status_code, 204)
