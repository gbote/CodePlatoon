"""helloDjango URL Configuration

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
import math
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rectangle_area(request):
    height = request.GET.get('height')
    width = request.GET.get('width')
    response = HttpResponse()
    if height is None or width is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The area of the rectangle is {int(height) * int(width)}.")
    return response

def rectangle_perimeter(request):
    height = request.GET.get('height')
    width = request.GET.get('width')
    response = HttpResponse()
    if height is None or width is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The perimeter of the rectangle is {(int(height)*2) + (int(width)*2)}.")
    return response

def circle_area(request):
    radius = request.GET.get('radius')
    response = HttpResponse()
    if radius is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The area of the circle is {int(radius)**2*math.pi}.")
    return response

def circle_perimeter(request):
    radius = request.GET.get('radius')
    response = HttpResponse()
    if radius is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The perimeter of the circle is {int(radius)*2*math.pi}.")
    return response

def rectangle_area2(request, height, width):
    response = HttpResponse()
    if height is None or width is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The area of the rectangle is {int(height) * int(width)}.")
    return response

def rectangle_perimeter2(request, height, width):
    response = HttpResponse()
    if height is None or width is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The perimeter of the rectangle is {(int(height)*2) + (int(width)*2)}.")
    return response

def circle_area2(request, radius):
    response = HttpResponse()
    if radius is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The area of the circle is {int(radius)**2*math.pi}.")
    return response

def circle_perimeter2(request, radius):
    response = HttpResponse()
    if radius is None:
        response.status_code = 409
    else:
        response = HttpResponse(f"<h1>The perimeter of the circle is {int(radius)*2*math.pi}.")
    return response

def home(request):
    return HttpResponse("<h1> Hello there! To calculate some shapes, structure your url like this: </h1> <h3>'/[circle | rectangle]/[area | perimeter]/[radius | length/width]'</h3> <h1>Fill in the parenthesis with your choices.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('rectangle/area/', rectangle_area),
    path('rectangle/perimeter/', rectangle_perimeter),
    path('circle/area/', circle_area),
    path('circle/perimeter/', circle_perimeter),
    path('rectangle/area/<int:height>/<int:width>', rectangle_area2),
    path('rectangle/perimeter/<int:height>/<int:width>', rectangle_perimeter2),
    path('circle/perimeter/<int:radius>', circle_perimeter2),
    path('circle/area/<int:radius>', circle_area2)
]