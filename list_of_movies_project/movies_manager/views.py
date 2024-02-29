from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter


class MovieViewSet(viewsets.ViewSet):
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filter_set_class = MovieFilter

    def list(self, request):
        paginator = self.pagination_class()
        movies = self.filter_set_class(request.GET, queryset=Movie.objects.all()).qs
        result_page = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
