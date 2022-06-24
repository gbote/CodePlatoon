from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os


load_dotenv()

pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.
def index(request):
    print('got a request!')
    # query the database to get the question_list
    # the keys on our data object can be accessed from the template

    print('env?')
    print(os.environ['apikey'])

    wish = request.GET.get('wish') or 'fish'

    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{wish}"

    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    # print(API_response.content)
    # print(responseJSON)
    # pp.pprint(responseJSON)
    preview_url = responseJSON['icon']['preview_url']
    return render(request, 'wishes_app/index.html', {'preview_url': preview_url, 'some-other-data': 4})