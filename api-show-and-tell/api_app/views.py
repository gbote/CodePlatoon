from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import requests as HTTPClient
import re

def widthheight(request): 
    winput = request.GET.get('widthinput')
    print(winput)
    hinput = request.GET.get('heightinput')
    print(hinput)
    url = (f"https://picsum.photos/{winput}/{hinput}")
    return redirect(f'https://picsum.photos/{winput}/{hinput}')

def index(request, width=400, height=400):
    # Params for the random imageg. Default will be 400 x 400
    PARAMS = {
        'HEIGHT': height,
        'WIDTH': width
    }
    api_img = (f"https://picsum.photos/{PARAMS['HEIGHT']}/{PARAMS['WIDTH']}")
    return render(request, 'base.html', {'api_img': api_img})

def about(request):
    return render(request, 'about.html')