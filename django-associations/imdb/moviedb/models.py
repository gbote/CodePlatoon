from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    actors = models.ManyToManyField(
        Actor, related_name="movies", through="Role")


class Role(models.Model):
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="roles")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="roles")
