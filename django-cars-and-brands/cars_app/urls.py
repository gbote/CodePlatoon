from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.brands_list, name="brands-list"),
    path("new/", views.new_brand, name="new-brand"),
    path("<int:brand_id>/", views.brand_list, name="brand-list"),
    path("<int:brand_id>/cars", views.brand_list, name="brand-cars"),
    path("<int:brand_id>/edit", views.brand_edit, name="brand-edit"),
    path("<int:brand_id>/cars/new", views.add_car, name="add-car"),
    path("<int:brand_id>/cars/<int:car_id>", views.display_car_details, name="display-car"),
    path("<int:brand_id>/cars/<int:car_id>/edit", views.edit_car, name="edit-car"),
]