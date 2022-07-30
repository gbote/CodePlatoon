import email
import imp
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import json
from .models import AppUser, TodoItem


def get_todo_items(user_id):
    todo_items_qset = TodoItem.objects.filter(app_user_id=user_id)
    todo_items = []
    for todo_item in todo_items_qset:
        todo_items.append({'id':todo_item.id, 'text':todo_item.text})
    return todo_items


def index(request):        
    login_field_dict = {}
    login_field_dict['email'] = {'label': 'Email address'}
    login_field_dict['password'] = {'label': 'Password'}
    login_field_dict['button'] = 'Login'
    signup_field_dict = {}
    signup_field_dict['email'] = {'label': 'Email address'}    
    signup_field_dict['email_description'] = 'We\'ll never share your email with anyone else.'
    signup_field_dict['password'] = {'label': 'Password (minlength=4)'}
    signup_field_dict['confirm_password'] = {'label': 'Re-enter password'}   
    signup_field_dict['button'] = 'Signup' 

    my_data = {'username': request.user.username, 'user_id': request.user.id, 'login_field': login_field_dict, 'signup_field': signup_field_dict}
    return render(request, 'todo/index.html', my_data)


@csrf_exempt
def signup(request):
    if request.method != 'POST':
        return(redirect(index))
    body = json.loads(request.body)
    try:
        user = AppUser.objects.create_user(username=body['email'],  email=body['email'], password=body['password'])
        login(request, user)
    except (ValidationError, IntegrityError) as e:
        return JsonResponse({'success': False, 'error': str(e)})        
    return JsonResponse({'success': True, 'todo_items': get_todo_items(user.id)})


@csrf_exempt
def log_in(request):
    if request.method != 'POST':
        return(redirect(index))
    body = json.loads(request.body)
    email = body['email']
    password = body['password']

    user = authenticate(username=email, password=password)
    if user:
        if user.is_active:
            try:
                login(request, user)
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
            return JsonResponse({'success': True, 'todo_items': get_todo_items(user.id)})
        else:
            return JsonResponse({'success': False, 'error': 'User is not active'})
    else:
        return JsonResponse({'success': False, 'error': 'email or password are incorrect'})


@csrf_exempt
def log_out(request):
    if request.method != 'POST':
        return(redirect(index))    
    logout(request)
    return JsonResponse({'success':True})


@csrf_exempt
def add_todo(request):
    if request.method != 'POST':
        return(redirect(index))
    body = json.loads(request.body)
    text = body['text']
    todo_item = TodoItem()
    todo_item.app_user_id = request.user.id
    todo_item.text = text
    try:
        todo_item.full_clean()
        todo_item.save()
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': True, 'todo_item': {'id':todo_item.id, 'text': todo_item.text}})


@csrf_exempt
def delete_todo(request):
    if request.method != 'POST':
        return(redirect(index))
    body = json.loads(request.body)
    todo_item_id = int(body['todo_item_id'])
    try:
        TodoItem.objects.filter(id=todo_item_id).delete()
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': True}) 
    

@csrf_exempt
def request_todo(request):
    if request.method != 'POST':
        return(redirect(index))
    return JsonResponse({'success': True, 'todo_items': get_todo_items(request.user.id)})