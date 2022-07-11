from django.shortcuts import render
from django.http import HttpResponse

from .models import Brand, Car

# Create your views here.
def brands(request):

    brands = Brand.objects.all()

    return render( request, 'index.html', {'brands': brands})

def cars(request):
    cars = Car.objects.all()

    return render( request, 'cars.html', {'cars': cars})

