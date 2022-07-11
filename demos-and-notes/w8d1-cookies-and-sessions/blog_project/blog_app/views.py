from django.shortcuts import render
import random
import datetime
import json
import hashlib
from django.http import JsonResponse
from .models import AppUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    print(request.COOKIES)
    return render(request, 'blog_app/index.html')

def set_cookies(request):
    response = render(request, 'blog_app/index.html')

    # cookie-key is foo, cookie-value is bar
    response.set_cookie('foo', 'bar', max_age=5)

    # httponly means the cookie cannot be accessed from javascript
    response.set_cookie('foo-2', 'bar-2', httponly=True)

    # a 'secure' cookie is only used over HTTPS. on HTTP, this cookie is completely ignored.
    # response.set_cookie('foo-2', 'bar-2', secure=True)

    return response


# sessions = {}
# def increment_count(request):
#     print(sessions)

#     session_id_number = request.COOKIES.get('session_id_number')
#     session = sessions.get(session_id_number)

#     if not session:
#         session_id_number = str(random.randint(100000,999999))

#         sessions[session_id_number] = {
#             'count': 1,
#             'start_time': datetime.datetime.now()
#         }
#     else:
#         sessions[session_id_number]['count'] += 1

#     response = render(request, 'blog_app/index.html', sessions[session_id_number])
#     response.set_cookie('session_id_number', session_id_number)
#     return response

def increment_count(request):
    if not request.session.get('count'):
        request.session['count'] = 1
        request.session['start_time'] = datetime.datetime.now().__str__()
    else:
        request.session['count'] += 1

    print(request.session['count'])
    print(request.session['start_time'])
    return render(request, 'blog_app/index.html', {
        'count': request.session.get('count'),
        'start_time': request.session.get('start_time')
    })

def generate_salt():
    return str(random.randint(10000000,99999999))


@csrf_exempt
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'blog_app/signup.html')

    elif request.method == 'POST':
        body = json.loads(request.body)
        raw_password = body['password']

        salt = generate_salt()

        salted_hashed_password = hashlib.sha256((salt + raw_password).encode()).hexdigest()

        new_user = AppUser(user_name=body['username'], password=f"{salt}${salted_hashed_password}")
        new_user.save()

        return JsonResponse({
            'success':True,
        })

@csrf_exempt
def log_in(request):
    if request.method == 'GET':
        return render(request, 'blog_app/login.html')
    elif request.method == 'POST':
        body = json.loads(request.body)
        user = AppUser.objects.get(user_name=body['username'])

        split_password = user.password.split('$')
        salt = split_password[0]
        hashed_password = split_password[1]

        challenge_hash = hashlib.sha256((salt + body['password']).encode()).hexdigest()

        if challenge_hash == hashed_password:
            response = JsonResponse({ 'success': True })

            response.set_cookie('user_id', user.id)
            return response