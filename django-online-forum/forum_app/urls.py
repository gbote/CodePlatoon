from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("post_details/<int:post_id>/", views.post_details, name="post_details"),
    path("add_post/", views.new_post, name="add_post"),
]