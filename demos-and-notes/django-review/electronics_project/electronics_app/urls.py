from django.urls import path
from . import views

urlpatterns = [
    # this route returns HTML
    path('', views.index),

    # this route returns JSON 
    path('products', views.products),

]