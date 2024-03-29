from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# from .models import Preference


from django.contrib.auth import authenticate, login, logout
from .models import AppUser as User

# we're not using django templates anymore
def send_the_homepage(request):
    print('home!')
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)


# when using @api_view, only logged-in users need CSRF tokens
@api_view(['POST'])
def sign_up(request):
    try:
        User.objects.create_user(username=request.data['email'], password=request.data['password'], email=request.data['email'])
    except Exception as e:
        print(e)
    return HttpResponse('hi')

@api_view(['POST'])
def log_in(request):
    print(dir(request))
    print(dir(request._request))

    # DRF assumes that the body is JSON, and automatically parses it into a dictionary at request.data
    email = request.data['email']
    password = request.data['password']
    # user = authenticate(username=email, password=password, email=email)
    user = authenticate(username=email, password=password)
    print('user?')
    print(user.email)
    print(user.password)
    if user is None:
        return HttpResponse('no user!')
    if user.is_active:
        try:
            # access the base request, not the DRF request
            # this starts a login session for this user
            login(request._request, user)
        except Exception as e:
            print('except')
            print(e)
        return HttpResponse('success!')
                # Redirect to a success page.
    else:
        return HttpResponse('not active!')
        # Return a 'disabled account' error message
        # Return an 'invalid login' error message.


@api_view(['POST'])
def log_out(request):
    logout(request)
    return HttpResponse('Logged you out!')


@api_view(['GET'])
def who_am_i(request):
    # Make sure that you don't send sensitive information to the client, such as password hashes
    # raise Exception('oops')
    if request.user.is_authenticated:
        data = serializers.serialize("json", [request.user], fields=['email', 'username'])
        return HttpResponse(data)
    else:
        return JsonResponse({'user':None})
