from django.shortcuts import render
from .helpers import get_poke
import random

def index(request):
    button_data = {
        'button': 'generate',
        'link': '/random'
    }
    return render(request, "poketeam/index.html", {"button_data": button_data})


def get_random_poke(request):
    poke_data = get_poke(random.randint(1, 151))
    team = poke_data[0]
    pokemon = poke_data[1]
    button = poke_data[2]
    return render(request, "poketeam/cards.html", {'pokemon': pokemon, 'team': team, 'button_data': button})


def get_poke_by_id(request, id):
    poke_data = get_poke(id)
    team = poke_data[0]
    pokemon = poke_data[1]
    button = poke_data[2]
    return render(request, "poketeam/cards.html", {'pokemon': pokemon, 'team': team, 'button_data': button})