from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
import pprint
import time

pp = pprint.PrettyPrinter(indent=2, depth=3)

# Create your views here.
def index(request):
    print("hello!")
    # wish = request.GET.get('wish') or 'fish'

    params = {
        'apikey': '86b674b3-f6c0-4040-9fec-dc395cd3cec8',

    }
    image_id = 60
    # print(API_response.status_code)
    responseJSON = {'error': 'Not found'}
    while responseJSON.get('error') == 'Not found':
        image_id += 1
        endpoint = f"https://api.harvardartmuseums.org/image/{image_id}"
        API_response = HTTP_Client.get(endpoint, params=params)
        responseJSON = API_response.json()
        pp.pprint(responseJSON)
        time.sleep(2)

    image_url = responseJSON['baseimageurl']
    return HttpResponse(f'<img src="{image_url}">')
