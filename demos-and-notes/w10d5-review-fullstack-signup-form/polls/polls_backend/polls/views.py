from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import AppUser

# Create your views here.
def index(request):
    print('home!')
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)

@api_view(['POST'])
def signup(request):
    print(request.data['email'])
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']

    AppUser.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['email'])
    

    return JsonResponse({'data': 'user was added'})

