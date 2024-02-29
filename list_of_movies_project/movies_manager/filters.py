import django_filters
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='year')
    directors = django_filters.CharFilter(field_name='directors__name')
    actors = django_filters.CharFilter(field_name='actors__name')

    class Meta:
        model = Movie
        fields = ['year', 'directors', 'actors']
