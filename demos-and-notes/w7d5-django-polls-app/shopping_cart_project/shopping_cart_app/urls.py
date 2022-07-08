from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cart-item/', views.cart_item ),
]