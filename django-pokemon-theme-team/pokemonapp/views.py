from django.shortcuts import render
from django.http import HttpResponse
import requests
import random
import pprint

pp = pprint.PrettyPrinter(indent = 2, depth = 2)

def getSix():  # sourcery skip: avoid-builtin-shadow
    type = random.randint(1,19)
    endpoint_type = f"https://pokeapi.co/api/v2/type/{type}"
    response = requests.get(endpoint_type)
    responseJSON = response.json()
    pokemon = responseJSON['pokemon']

    len_poke = len(pokemon)
    data = []

    for _ in range(6):
        randomPoke = random.randint(0,len_poke)
        endpoint_poke = pokemon[randomPoke]["pokemon"]["url"]
        responseRandom = requests.get(endpoint_poke)
        responseJSONRandom = responseRandom.json()
        name = responseJSONRandom["name"]
        image = responseJSONRandom["sprites"]["front_default"]

        data.append({'name': name, 'image': image})

    return data


# getSix()

def index(request):
    data = getSix()
    return render(request, 'index.html', {'data' : data})