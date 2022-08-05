from django.urls import path
from . import views

urlpatterns = [
    # serves index.html which will load our react app
    path('', views.index),
    # API endpoints - return JSON data
    path('grades/', views.get_grades),
    path('assignments/', views.get_assignments),
    path('assignments/<int:assignment_id>', views.get_assignment)
]
