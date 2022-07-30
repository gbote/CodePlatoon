from pyexpat import model
from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    year = models.IntegerField(max_length=4)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.model}"
