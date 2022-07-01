from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from requests_oauthlib import OAuth1
import json
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ)
# Create your views here.
def index(request):
    # query the database to get the question_list
    # the keys on our data object can be accessed from the template
    response = render(request, 'electronics_app/index.html')
    return response

def products(request):

    # GET requests can't have a body. We have to look for the data in the URL. 
    print(request.GET.get('query'))
    query = request.GET.get('query')

    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    print(API_response.content)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url })
