from django.urls import path
from . import views


urlpatterns = [
    path("brands/", views.brands, name="brands"),
    path("brands/<int:detail_id>", views.brand_detail, name="brand_detail"),
    path("brands/<int:edit_id>/edit", views.brand_edit, name="brand_edit"),
    path("cars/<int:detail_id>", views.car_detail, name="car_detail"),
    path("cars/<int:edit_id>/edit", views.car_edit, name="car_edit"),
    path("cars/<int:brand_id>/new", views.car_new, name="car_new"),
]
