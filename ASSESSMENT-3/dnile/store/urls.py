from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('baby-kids/', views.baby, name='baby-kids'),
    path('bed-bath/', views.bed, name='bed-bath'),
    path('furniture/', views.furniture, name='furniture'),
    path('kitchen-dining/', views.kitchen, name='kitchen-dining'),
    path('office/', views.office, name='office'),
    path('search/', views.search, name='search'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
]