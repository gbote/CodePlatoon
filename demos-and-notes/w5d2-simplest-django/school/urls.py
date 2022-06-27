"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Example of a basic route handler function
def my_route_handler(request):
  response = HttpResponse("<h1>Hello, world!</h1>")
  print('---------request-------------')
  print(dir(request))
  print('---------response-------------')
  print(dir(response))

  return response

def rootRouteHandler(request):
  print('root route handler')
  print(request.path)
  response = HttpResponse("<marquee>Welcome to my Django page!</marquee>")
  return response

# Example of route handler function using an URL param
def user_login(request, username):
  # Talk to database, get user info
  response = HttpResponse(f"<h1>Hello, {username}</h1>")

  # Example of how we can use conditional logic to set the response
  # status code.
  if(username == 'teapot'):
    response.status_code = 418

  return response

# Example of using query params in route handler function
def another_cool_route_handler(request):
  response = HttpResponse(f"<p>Hello world!</p>")

  # Accessing query params
  foo = request.GET.get('foo')
  bar = request.GET.get('bar')

  # Printing them to terminal
  print('foo: ' + foo)
  print('bar: ' + bar)

  return response

urlpatterns = [
    # root path '/'
    path('', rootRouteHandler),

    # Example of a basic path
    path('my-route/', my_route_handler),

    #Example of path with an URL param
    path('user-login/<str:username>', user_login),

    # Notice how the route handler function uses
    # Query params, but we don't have to do anything special
    # with out path.
    path('another-cool-route/', another_cool_route_handler),

    # Example of how you can have two different paths
    # point to the same route handler function --
    # the path 'admin/' points to the same function this does.
    path('my-awesome-admin/', admin.site.urls),

    path('admin/', admin.site.urls),
]
