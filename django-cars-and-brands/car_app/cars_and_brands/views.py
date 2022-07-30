from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ValidationError
from .models import *
import re

# Create your views here.
def brands(request):
    my_data = {}

    if request.method == "POST":
        try:
            new_brand = Brand()
            new_brand.name = request.POST["brand"]
            new_brand.full_clean()
            new_brand.save()

        except ValidationError as ve:
            my_data["error"] = ve.message_dict

    my_data["all_brands"] = Brand.objects.order_by("name")

    return render(request, "pages/brands.html", my_data)


def brand_detail(request, detail_id):
    my_data = {}

    my_data["brand"] = Brand.objects.get(pk=detail_id)

    return render(request, "pages/brand_detail.html", my_data)


def brand_edit(request, edit_id):
    my_data = {}

    if request.method == "POST":
        try:
            update_brand = Brand.objects.get(id=edit_id)
            update_brand.name = request.POST["brand"]
            update_brand.full_clean()
            update_brand.save()

            for car in request.POST:
                pattern = r"car-(\d+)"
                match = re.search(pattern, car)
                if match:
                    update_car = Car.objects.get(id=match.group(1))
                    update_car.model = request.POST[car]
                    update_car.full_clean()
                    update_car.save()
            return redirect(reverse("brand_detail", args=(edit_id,)))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict

    my_data["brand"] = Brand.objects.get(pk=edit_id)

    return render(request, "pages/brand_edit.html", my_data)


def car_detail(request, detail_id):
    my_data = {}
    my_data["car"] = Car.objects.get(id=detail_id)

    return render(request, "pages/car_detail.html", my_data)


def car_edit(request, edit_id):
    my_data = {}

    if request.method == "POST":
        try:
            update_car = Car.objects.get(id=edit_id)
            update_car.year = request.POST["year"]
            update_car.color = request.POST["color"]
            update_car.model = request.POST["model"]
            update_car.full_clean()
            update_car.save()

            return redirect(reverse("car_detail", args=(edit_id,)))
        except ValidationError as ve:
            my_data["error"] = ve.message_dict

    my_data["car"] = Car.objects.get(id=edit_id)
    return render(request, "pages/car_edit.html", my_data)


def car_new(request, brand_id):
    my_data = {}
    if request.method == "POST":
        try:
            add_new_car = "add_new" in request.POST
            if add_new_car:

                new_car = Car()
                new_car.model = request.POST["model"]
                new_car.color = request.POST["color"]
                new_car.year = request.POST["year"]
                new_car.brand = Brand.objects.get(id=brand_id)
                new_car.full_clean()
                new_car.save()

            return redirect(reverse("brand_detail", args=(brand_id,)))

        except ValidationError as ve:
            my_data["error"] = ve.message_dict

    my_data["car"] = Brand.objects.get(id=brand_id)
    return render(request, "pages/car_new.html", my_data)
