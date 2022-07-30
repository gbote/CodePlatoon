from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('delete_todo', views.delete_todo, name='delete_todo'),
    path('request_todo', views.request_todo, name='request_todo'),
]