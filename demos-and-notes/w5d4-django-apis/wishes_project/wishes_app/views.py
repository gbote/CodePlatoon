from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os
from django.views.decorators.csrf import csrf_exempt
import json


load_dotenv()

pp = pprint.PrettyPrinter(indent=2, depth=2)


# Create your views here.
def index(request):


    print('got a request!')
    # query the database to get the question_list
    # the keys on our data object can be accessed from the template

    print('env?')
    print(os.environ['apikey'])

    wish = request.GET.get('wish') or 'fish'

    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{wish}"

    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    # print(API_response.content)
    # print(responseJSON)
    # pp.pprint(responseJSON)
    preview_url = responseJSON['icon']['preview_url']
    if os.environ['env'] == 'prod':
        # send emails, only in prod
        pass

    response = render(request, 'wishes_app/index.html', {'preview_url': preview_url, 'some-other-data': 4})
    return response



@csrf_exempt
def show_me_pokemon(request):

    if request.method == 'POST':
        # print(request.POST)
        # print(request.body)
        body = json.loads(request.body)
        # content = body['content']
        print(body)
        pokemon_name = body['pokemonName']

        endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

        API_response = HTTP_Client.get(endpoint)
        responseJSON = API_response.json()

        pp.pprint(responseJSON)
    
        print(responseJSON['sprites']['front_shiny'])
        return JsonResponse({'image_url': responseJSON['sprites']['front_shiny']})

    # should probably throw an error if we receive the wrong request type
    return HttpResponse("Got it!")