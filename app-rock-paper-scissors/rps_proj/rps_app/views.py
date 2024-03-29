from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import AppUser as User
from rest_framework.decorators import api_view
from django.core import serializers
from .models import Throw, Game

# Create your views here.

def send_the_homepage(request):
    print('home!')
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)


@api_view(['POST'])
def sign_up(request):

    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    try:
        User.objects.create_user(username=username, email=email, password=password)

    except Exception as e:
        print(e)
    return JsonResponse({'data': '{user} has signed up!'})


@api_view(['POST'])
def log_in(request):
    print(dir(request))
    print(dir(request._request))
    email = request.data['email']
    password = request.data['password']
    user = authenticate(username=email, password=password)
    print('user?')
    print(user.email)
    print(user.password)
    if user is None:
        return HttpResponse('no user!')
    if user.is_active:
        try:
            login(request._request, user)
        except Exception as e:
            print('except')
            print(e)
        return HttpResponse('success!')
    else:
        return HttpResponse('not active!')
        # Return an 'invalid login' error message.


@api_view(['POST'])
def log_out(request):
    logout(request)
    return JsonResponse({'success': True})
    # return HttpResponse('Logged you out!')



@api_view(['GET'])
def who_am_i(request):
    # Make sure that you don't send sensitive information to the client, such as password hashes
    # raise Exception('oops')
    if request.user.is_authenticated:
        data = serializers.serialize("json", [request.user], fields=['email', 'username'])
        return HttpResponse(data)
    else:
        return JsonResponse({'user':None})


@api_view(['POST'])
def start_new_game(request):
    victory_num = request.data['victoryNumber']
    total_throws = request.data['totalThrows']
    try:
        game = Game.objects.create(victory_num=victory_num, total_throws=total_throws)
    except Exception as e:
        print(e)
    return JsonResponse({'gameID': game.id})


@api_view(['GET'])
def play_game(request, game_id):
    game = None
    try:
        game = Game.objects.get(id=game_id)
        print(game)
        data = {'victory_num': game.victory_num, 'total_throws': game.total_throws}
        return JsonResponse(data=data)
    except Exception as e:
        print(e)
    return JsonResponse({'game': None})