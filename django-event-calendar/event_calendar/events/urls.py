from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'events'
urlpatterns = [
  path('', views.home, name='home'),
  path('create_event/', views.create_event, name='create_event'),
  path('view_all_events/', views.view_all_events, name='view_all_events'),
  path('edit_event/<int:id>', views.edit_event, name='edit_event'),
  path('delete_event/<int:id>', views.delete_event, name='delete_event'),
  path('view_event/<int:id>', views.view_event, name='view_event')
]