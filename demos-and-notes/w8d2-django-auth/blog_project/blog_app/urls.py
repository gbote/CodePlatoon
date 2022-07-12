from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('whoami', views.whoami),

]
