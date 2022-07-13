from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('videos/', views.get_videos),
    path('customers/', views.get_customers),
    path('customer/<int:customer_id>/', views.get_customer),
    path('add-customer/', views.add_customer),
    path('rent/', views.rent_video),
    path('return/', views.return_video),

]