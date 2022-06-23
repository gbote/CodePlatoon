from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path('random', views.get_random_poke),
    path("<int:id>/", views.get_poke_by_id, name="get_poke_by_id"),
]