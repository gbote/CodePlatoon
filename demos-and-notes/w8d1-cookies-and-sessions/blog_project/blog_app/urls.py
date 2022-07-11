from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('set-cookies', views.set_cookies),
    path('increment-count', views.increment_count),
    path('sign-up', views.sign_up),
    path('log-in', views.log_in),
    
]