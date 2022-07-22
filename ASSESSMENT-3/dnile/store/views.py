from django.shortcuts import render
import requests as HTTP_Client
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os
from django.http import JsonResponse
import json

load_dotenv()

departments = [
    {
        "name": "kitchen & dining",
        "url_name": "kitchen-dining",
        "products": [
            {
                "id": 0,
                "product": "cookware set",
                "name": "Caraway Home Silt Green 7-Piece Non-Stick Ceramic Cookware Set",
                "price": 545.00,
                "image_loc": "store/images/caraway_cookware_set.jpg"
            },
            {
                "id": 1,
                "product": "kitchen knife set",
                "name": "Miyabi 10-Piece Knife Set",
                "price": 525.00,
                "image_loc": "store/images/miyabi_knife_set.jpg"
            },
            {
                "id": 2,
                "product": "tea kettle",
                "name": "Simplex Buckingham No. 1 Copper Rapid Boil Tea Kettle",
                "price": 399.95,
                "image_loc": "store/images/simplex_buckingham_kettle.jpg"            
            },
            {
                "id": 3,
                "product": "dinnerware set",
                "name": "Royal Albert Old Country Roses 20-Piece Dinnerware Set",
                "price": 525.00,
                "image_loc": "store/images/royal_albert_dinnerware_set.jpg"
            },
        ]
    },
    {
        "name": "furniture",
        "url_name": "furniture",
        "products": [
            {
                "id": 100,
                "product": "rocking chair",
                "name": "Hand-Crafted Walnut Rocking Chair",
                "price": 10000.00,
                "image_loc": "store/images/walnut_rocking_chair.jpg" 
            },
            {
                "id": 101,
                "product": "sofa",
                "name": "Peugeot Onyx Sofa",
                "price": 185000.00,
                "image_loc": "store/images/peugeot_onyx_sofa.jpg"

            },
            {
                "id": 102,
                "product": "coffee table",
                "name": "Boca do Lobo Lapiaz Oval Coffee Table",
                "price": 10730.00,
                "image_loc": "store/images/lapiaz-oval-center-table.png"
            },
        ],
    },
    {
        "name": "bed & bath",
        "url_name": "bed-bath",
        "products": [
            {
                "id": 200,
                "product": "bed",
                "name": "Maitland-Smith Orleans Bed",
                "price": 24747.75,
                "image_loc": "store/images/orleans_bed.jpg"
            },
            {
                "id": 201,
                "product": "chest of drawers",
                "name": "Chippendale Mahogany Chest of Drawers",
                "price": 7853.00,
                "image_loc": "store/images/chippendale_drawers.jpg"
            },
            {
                "id": 202,
                "product": "tub",
                "name": "'The Cathryn Adele68' 68-inch Cast Iron French Bateau Clawfoot Tub plus Drain",
                "price": 5195.00,
                "image_loc": "store/images/cathryn_adele_68in_clawfoot_tub.jpg"            
            },
        ],
    },
    {
        "name": "office",
        "url_name": "office",
        "products": [
            {
                "id": 300,
                "product": "desk",
                "name": "David Micahel 90-inch Executive Desk",
                "price": 52584.53,
                "image_loc": "store/images/david_michael_desk.jpg"
            },
            {
                "id": 301,
                "product": "office chair",
                "name": "Old Hickory Tannery Executive Chair",
                "price": 7560.00,
                "image_loc": "store/images/old_hickory_tannery_office_chair.jpg"
            },
            {
                "id": 302,
                "product": "desk lamp",
                "name": "Meyda Tiffany Utica 17-inch Black Lamp with USB",
                "price": 6300.00,
                "image_loc": "store/images/meyda_tiffanny_desk_lamp.jpg"            
            }
        ],
    },
    {
        "name": "baby & kids",
        "url_name": "baby-kids",
        "products": [
            {
                "id": 400,
                "product": "crib",
                "name": "Art-For-Kids Seashore Crib",
                "price": 3200.00,
                "image_loc": "store/images/ArtForKids_Seashore_Crib.jpg"
            },
            {
                "id": 401,
                "product": "playset",
                "name": "Kid’s Creations Adventure Mountain Redwood Playset",
                "price": 13999.00,
                "image_loc": "store/images/kids-creation-backyard-playset.jpeg"
            },
            {
                "id": 402,
                "product": "puppy",
                "name": "Naughty Puppy",
                "price": 0.00,
                "pretty_price": "$|_0\/3",
                "image_loc": "store/images/puppy_trouble.jpg"            
            },
        ]
    }
]

for dept in departments:
    for product in dept["products"]:
        if "pretty_price" not in product:
            product["pretty_price"] = "${:,.2f}".format(product["price"])

cart_items = {
    'products':[],
    'total_items': 0,
    'total_charge': 0,
    }

def index(request):
    context = { 'categories': departments }
    return render(request, 'store/index.html', context)

def baby(request):
    context = { 'products': departments[4]["products"] }
    return render(request, 'store/baby-kids.html', context)

def bed(request):
    context = { 'products': departments[2]["products"] }
    return render(request, 'store/bed-bath.html', context)

def furniture(request):
    context = { 'products': departments[1]["products"]}
    return render(request, 'store/furniture.html', context)

def kitchen(request):
    context = { 'products': departments[0]["products"] }
    return render(request, 'store/kitchen-dining.html', context)

def office(request):
    context = { 'products': departments[3]["products"] }
    return render(request, 'store/office.html', context)

def search(request):
    found_products = []
    not_available_icon = ""
    search_term = request.POST['search_term']
    for department in departments:
        found_products.extend(product for product in department['products'] if search_term.lower() in product['name'].lower())

    if not found_products:
        auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
        endpoint = f"http://api.thenounproject.com/icon/{search_term}"
        API_response = HTTP_Client.get(endpoint, auth=auth)
        responseJSON = API_response.json()
        not_available_icon = responseJSON["icon"]["preview_url"]
    context = { 'search_term': search_term, 'products': found_products, 'icon': not_available_icon }
    return render(request, 'store/search.html', context)

def get_product(id):
    for dept in departments:
        for product in dept["products"]:
            if product["id"] == int(id):
                return product

def add_to_cart(request):
    if request.method == "POST":
        # print(f"<=-- DATA FROM JS: {request.POST.get('product_id')} --=>")
        # print(f"<=-- DATA FROM JS: {request.POST['product_id']} --=>") # equivalent to above
        product_id = request.POST.get('product_id')
        if product_id in cart_items:
            cart_items[product_id] += 1
            for product in cart_items['products']:
                if str(product['id']) == product_id:
                    product['quantity'] += 1
                    product['subtotal'] += product['price']
                    product['pretty_subtotal'] = "${:,.2f}".format(product['subtotal'])
        else:
            product = get_product(product_id)
            product['quantity'] = 1
            product['subtotal'] = product['price']
            product['pretty_subtotal'] = "${:,.2f}".format(product['subtotal'])
            cart_items['products'].append(product)
            cart_items[product_id] = 1
        cart_items['total_items'] += 1
        cart_items['total_charge'] += product['price']
        cart_items['pretty_total'] = "${:,.2f}".format(cart_items['total_charge'])
    context = {'cart': cart_items}
    ##### FIX: DOES NOT GO TO CART PAGE AFTER 'ADD TO CART' #####
    # OR UPDATE QTY IN DOM
    return render(request, 'store/cart.html', context)

def cart(request):
    context = cart_items
    return render(request, 'store/cart.html', context)