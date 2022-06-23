import requests


def get_poke(param):
    button_data = {
        'button': 'clear',
        'link': '/'
    }
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{param}/")
    responseJSON = response.json()
    pokemon = {
        'name': responseJSON['name'],
        'type': responseJSON['types'][0]['type']['name'],
        'img': responseJSON['sprites']['front_default'],
    }
    team = [pokemon]
    print("team: ", team)
    all_of_type = responseJSON['types'][0]['type']['url']
    type_data = requests.get(all_of_type).json()
    count = 0
    for i in type_data['pokemon']:
        if count == 5:
            break
        url = i['pokemon']['url']
        pokemon_data = requests.get(str(url))
        pokemon_dataJSON = pokemon_data.json()
        teammate = {
            'name': pokemon_dataJSON['name'],
            'img': pokemon_dataJSON['sprites']['front_default'],
        }
        team.append(teammate)
        count += 1
    return [team, pokemon, button_data]
