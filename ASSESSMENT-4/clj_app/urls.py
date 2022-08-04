from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_categories, name = "list_categories"),
    path('categories', views.list_categories, name = "list_categories"),
    path('categories/new/', views.add_category, name = "add_category"),
    path('categories/<int:category_id>/view', views.list_posts, name = "list_posts"),
    path('categories/<int:category_id>/edit', views.edit_category, name = "edit_category"),
    path('categories/<int:category_id>/posts/<int:post_id>/view', views.post_info, name = "post_info"),
    path('<int:category_id>/posts/<int:post_id>/edit/', views.edit_post, name = "edit_post"),
    path('categories/<int:category_id>/posts/new', views.add_post, name = "add_post")
]
