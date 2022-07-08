from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up', views.sign_up, name="signup"),
    path('login', views.log_in, name='login'),
    path("success", views.success, name="success"),
    path("logout", views.logout_user, name="logout_user"),
]