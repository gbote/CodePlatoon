from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json


from .models import Item, Cart, CartItem

# is called when we go to our root url in the browser
def index(request):

    cart_id = 1                             # hardcoded cart ID
    items = Item.objects.all()              # get list of all items
    cart = Cart.objects.get(id=cart_id)     # get cart object with our cart ID

    data  = []

    # loop through items and create a dictionary in form of {'item': ... , 'quantity': ...}
    for item in items:
        item_dict = {}
        item_dict['item'] = item
        # try getting a cart item if it exists and get item quantity
        try:
            c_item = CartItem.objects.get(cart= cart, item = item)
            item_dict['quantity'] = c_item.quantity
        #else set quantity to 0
        except:
            item_dict['quantity'] = 0

        data.append(item_dict)

        print(item_dict)
    

    #  = {'items': items}
    
    return render(request, 'shopping_cart_app/index.html', {'data': data} )

@csrf_exempt
# this function creates a cartItem / updates a cartItem quantity
def cart_item(request):
    cart_id = 1
    
    # here we json.loads to access the data since the request was sent throug axios with js 
    # the request arrives in a different format than a 'POST' request sent from the html pages
    body = json.loads(request.body) 
    item_id = body['item_id']

    cart = Cart.objects.get(id = cart_id)
    item = Item.objects.get(id = item_id)

    # if cart item already exists, update
    try:
        c_item = CartItem.objects.get(cart= cart, item = item)
        c_item.quantity += 1
        c_item.full_clean()
        c_item.save()

    # else create new
    except:
        c_item = CartItem(cart = cart, item = item)
        c_item.full_clean()
        c_item.save()

    return  JsonResponse({'item_id': c_item.item.id, 'item_quantity':c_item.quantity})