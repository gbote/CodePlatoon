import re
from django.forms import ValidationError
from django.shortcuts import redirect, render, reverse
from .models import Brand, Car

from cars_app.models import Brand

# Create your views here.
def brands_list(request):
    my_data = {"all_brands": Brand.objects.all()}
    return render(request, "pages/brands_list.html", my_data)


def new_brand(request):
    my_data = {"all_brands": Brand.objects.all()}
    if request.method == "POST":
        try:
            nb = Brand()
            nb.make_name = request.POST["new_brand"] 
            nb.full_clean()
            nb.save()
        except ValidationError as ve:
            my_data["error"] = ve.message_dict
        return redirect(reverse("brands-list"))
    return render(request, "pages/new_brand.html", my_data)


def brand_list(request, brand_id):
    my_data = {}
    if request.method == "POST":
        do_delete = "delete_brand" in request.POST
        try:
            if do_delete:
                brand_id_to_delete = request.POST["delete_brand"]
                Brand.objects.get(id=brand_id_to_delete).delete()
            return redirect(reverse("brands-list"))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict        
    my_data["all_brands"] = Brand.objects.all()
    my_data["brand"] = Brand.objects.get(id=brand_id)
    return render(request, 'pages/brand_list.html', my_data)


def brand_edit(request, brand_id):
    my_data = {"all_brands": Brand.objects.all()}
    if request.method == "POST":
        try:
            b = Brand.objects.get(pk=brand_id)
            b.make_name = request.POST["brand"]
            b.full_clean()
            b.save()
            return redirect(reverse("brand-list", args=(brand_id, )))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict
    my_data["brand"] = Brand.objects.get(id=brand_id)
    return render(request, "pages/brand_edit.html", my_data)


def add_car(request, brand_id):
    my_data = {"all_brands": Brand.objects.all()}
    if request.method == "POST":
        try:
            new_car_to_add = "add_car" in request.POST
            c = Car()
            c.model = request.POST["car"]
            c.make = Brand.objects.get(id=brand_id)
            c.full_clean()
            c.save()
            return redirect(reverse("brand-list", args=(brand_id, )))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict            

    my_data["brand"] = Brand.objects.get(id=brand_id)
    return render(request, "pages/add_car.html", my_data)

def display_car_details(request, brand_id, car_id):
    my_data = {}
    if request.method == "POST":
        do_delete = "delete_car" in request.POST
        try:
            if do_delete:
                car_id_to_delete = request.POST["delete_car"]
                Car.objects.get(id=car_id_to_delete).delete()
            return redirect(reverse("brand-list", args=(brand_id,)))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict        
    my_data["all_brands"] = Brand.objects.all()
    my_data["brand"] = Brand.objects.get(id=brand_id)
    my_data["car"] = Car.objects.get(id=car_id)

    return render(request, 'pages/car_detail.html', my_data)


def edit_car(request, brand_id, car_id):
    my_data = {"all_brands": Brand.objects.all()}

    my_data["brand"] = Brand.objects.get(id=brand_id)
    my_data["car"] = Car.objects.get(id=car_id)


    if request.method == "POST":
        try:
            c = Car.objects.get(pk=car_id)
            c.model = request.POST["car"]
            c.full_clean()
            c.save()

            return redirect(reverse("display-car", args=(brand_id, car_id, )))

        except ValidationError as ve:
            my_data["error"] = ve.message_dict

    return render(request, "pages/car_edit.html", my_data)