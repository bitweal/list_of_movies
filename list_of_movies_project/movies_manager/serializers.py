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
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'directors', 'actors')

    def create(self, validated_data):
        directors_data = validated_data.pop('directors')
        actors_data = validated_data.pop('actors')

        movie = Movie.objects.create(**validated_data)

        for director_data in directors_data:
            director_name = director_data.get('name')
            director, _ = Director.objects.get_or_create(name=director_name)
            movie.directors.add(director)

        for actor_data in actors_data:
            actor_name = actor_data.get('name')
            actor, _ = Actor.objects.get_or_create(name=actor_name)
            movie.actors.add(actor)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)

        directors_data = validated_data.pop('directors', [])
        actors_data = validated_data.pop('actors', [])

        instance.directors.clear()
        instance.actors.clear()

        for director_data in directors_data:
            director_name = director_data.get('name')
            director, _ = Director.objects.get_or_create(name=director_name)
            instance.directors.add(director)

        for actor_data in actors_data:
            actor_name = actor_data.get('name')
            actor, _ = Actor.objects.get_or_create(name=actor_name)
            instance.actors.add(actor)

        instance.save()
        return instance
