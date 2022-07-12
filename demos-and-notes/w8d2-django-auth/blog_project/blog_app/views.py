from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AppUser as User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

def index(request):
    if request.user.is_authenticated:
        return render(request, 'blog_app/index.html', model_to_dict(request.user))
    else:
        return render(request, 'blog_app/index.html')

@csrf_exempt
def signup(request):
    print('hello!')
    if request.method == 'GET':
        return render(request, 'blog_app/signup.html')

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            User.objects.create_user(username=body['username'], email=body['email'], password=body['password'])
            return JsonResponse({'success':True})
        except Exception as e:
            print('oops!')
            print(str(e))
            return JsonResponse({'Success':False})


@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request, 'blog_app/login.html')
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']

        # this doesn't start a login session, it just tells us which user from the db belongs to these credentials
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                    # this method actually sets a cookie to start a session
                    login(request,user)
                    print('logged in!')
                    return JsonResponse({'Success': True})
                except Exception as e:
                    return JsonResponse({'Success': False, 'reason': 'login failed'})
            else:
                return JsonResponse({'Success': False, 'reason': 'account disabled'})
        else:
            return JsonResponse({'Success': False, 'reason': 'user does not exist'})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def whoami(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'email': request.user.email,
        })
    else:
        return JsonResponse({'email':None})
