from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    directors = models.ManyToManyField(Director, related_name='directors')
    actors = models.ManyToManyField(Actor, related_name='actors')

    def __str__(self):
        return self.title
