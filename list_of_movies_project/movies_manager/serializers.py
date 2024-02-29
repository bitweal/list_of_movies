from rest_framework import serializers
from .models import Director, Actor, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'director', 'actors')
