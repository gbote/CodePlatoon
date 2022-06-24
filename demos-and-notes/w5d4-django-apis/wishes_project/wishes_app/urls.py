from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show-me-pokemon', views.show_me_pokemon)
]

