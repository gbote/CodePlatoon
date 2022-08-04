from django.urls import path, include

urlpatterns = [
    path('', include('clj_app.urls'))
]
