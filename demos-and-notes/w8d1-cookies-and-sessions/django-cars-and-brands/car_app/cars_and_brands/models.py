from django.db import models


def car_year_validator(input):
    return input > 1800


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Car(models.Model):
    brand = models.ForeignKey( Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    year = models.IntegerField(validators=[car_year_validator])

    

