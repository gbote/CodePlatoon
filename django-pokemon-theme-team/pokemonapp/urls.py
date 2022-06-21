from logging import root
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]