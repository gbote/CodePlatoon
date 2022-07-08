from django.db import models


class Brand(models.Model):
    make_name = models.CharField(max_length=64)
    #models field created due to FK models in Car class

    def __str__(self):
        return f'{self.make_name}'

class Car(models.Model):
    model = models.CharField(max_length=64)
    make = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return f'{self.model}'