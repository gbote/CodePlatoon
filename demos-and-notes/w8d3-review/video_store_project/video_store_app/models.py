from enum import unique
from ntpath import realpath
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200, unique=True)
    rating = models.CharField(max_length=10)
    release_year = models.CharField( max_length=4)
    copies_available = models.IntegerField()


class Customer(models.Model):
    rentals = models.ManyToManyField(Video, through='Rental')
    first_name = models.CharField( max_length=200)
    last_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=2)


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('customer', 'video'))

