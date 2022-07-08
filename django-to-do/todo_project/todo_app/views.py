import re
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AppUser, Todo_Items 
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def index(request):
    print("current user? ", request.session.items())
    return render(request, 'pages/index.html')


@csrf_exempt
def sign_up(request):
    my_data = {}
    if request.method == 'GET':
        return render(request, 'pages/signup.html')
    elif request.method == 'POST':
        body = json.loads(request.body)
        try:
            check = validate_email(body['email'])
            if check is None:
                user = AppUser.objects.create_user(username=body['email'],  email=body['email'], password=body['password'])
                login(request,user)
                my_data["user"]=user
                my_data["user_id"]=user.id
                if "anon_todos" not in request.session:
                    print("anon_todos do not exist")
                elif request.session["anon_todos"] == []:
                    del request.session["anon_todos"]
                    del request.session["anon_user"]
                    request.session.modified = True
                else:
                    for item in request.session["anon_todos"]:
                        new_td = Todo_Items()
                        new_td.contents = item
                        new_td.user_id = AppUser.objects.get(id=user.id)
                        new_td.full_clean()
                        new_td.save()
                    del request.session["anon_todos"]
                    del request.session["anon_user"]
                    request.session.modified = True
                    my_data["user_todos"] = Todo_Items.objects.filter(user_id=user.id)
                return JsonResponse({ 'success':True })
        except ValidationError as ve:
            return JsonResponse({'success': False})
    return render(request, 'pages/sign-up.html', my_data)


@csrf_exempt
def log_in(request):
    my_data = {}
    if request.method == "POST":
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            if not user.is_active:
                return JsonResponse({'success':False})
            try:
                login(request,user)
                my_data["user"]=user
                my_data["user_id"]=user.id
                if request.session["anon_todos"] != []:
                    for item in request.session["anon_todos"]:
                        new_td = Todo_Items()
                        new_td.contents = item
                        new_td.user_id = AppUser.objects.get(id=user.id)
                        new_td.full_clean()
                        new_td.save()
                del request.session["anon_todos"]
                del request.session["anon_user"]
                request.session.modified = True
                return redirect(reverse("success", my_data))

            except Exception as e:
                return JsonResponse({'success': True})
        else:
            print('user does not exist')
            return JsonResponse({'success':False})
    elif request.method == "GET":
        return render(request,'pages/login.html', my_data)


@csrf_exempt
def success(request):  # sourcery skip: low-code-quality
    my_data = {"user_todos": []}
    if "_auth_user_id" in request.session:
        current_user = request.session['_auth_user_id']
        my_data["user_todos"] = Todo_Items.objects.filter(user_id=current_user)
    else:
        print("is authorized user entering first else? Should not!")
        if 'anon_todos' not in request.session or not request.session['anon_todos']:
            request.session['anon_user'] = 'anon_user'
            request.session['anon_todos'] = []
        else:
            my_data["user_todos"] = request.session['anon_todos']

        current_user = request.session['anon_user']

    my_data["current_user"] = current_user

    print("sessions items in success before get request: ", request.session.items())
    print("mydata before get: ", my_data["user_todos"])

    if request.method == "GET":
        return render(request, 'pages/success.html', my_data)

    if request.method == "POST":

        body = json.loads(request.body)
        print("body: ", body)

        if "delete_todo" in body:
            print("deleting todo...")
            if "anon_todos" in request.session:
                anon_todo_to_delete = body["delete_todo"]
                request.session["anon_todos"].remove(anon_todo_to_delete)
                request.session.modified = True
                my_data["user_todos"] = request.session["anon_todos"]

            else:
                Todo_Items.objects.filter(contents=body["delete_todo"], user_id=current_user).delete()
            return JsonResponse({'success':True})

        else:
            new_todo = body['todo']
            if new_todo=="":
                return JsonResponse({'success': False})
            if "_auth_user_id" in request.session:
                td = Todo_Items()
                td.contents = new_todo
                td.user_id = AppUser.objects.get(id=current_user)
                td.full_clean()
                td.save()
                return JsonResponse({'success': True, 'todo_to_add': td.contents })
            else:
                request.session['anon_todos'].append(new_todo)
                request.session.modified = True
                my_data["user_todos"] = request.session['anon_todos']
                return JsonResponse({'success': True, 'todo_to_add': new_todo })
    return render(request, 'pages/success.html', my_data)


def logout_user(request):
    logout(request)
    print("logged out? ", request.session.items())
    return render(request, 'pages/index.html')