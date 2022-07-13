from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


import json
from .models import Customer, Video, Rental

def index(request):
    return render(request, 'index.html')


def get_videos(request):

    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def get_customers(request):
    customers = Customer.objects.all()

    return render(request, 'customers.html', {'customers': customers})


def get_customer(request, customer_id):

    customer = Customer.objects.get(id = customer_id)
    videos = customer.rentals.all()

    print(videos)

    data = {'customer': customer, 'videos': videos}
    return render(request, 'customer.html', data)

@csrf_exempt
def add_customer(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)

        customer = Customer(
            first_name = data['first_name'],
            last_name = data['last_name'],
            account_type = data['account_type']
        )

        customer.full_clean()
        customer.save()

        response = {
            'data': model_to_dict(customer),
            'success': 'True'
        }

    return JsonResponse(response)


def rent_video(request):
    return HttpResponse('hello')


def return_video(request):
    return HttpResponse('hello')




