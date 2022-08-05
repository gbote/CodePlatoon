from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Assignment, Grade

# Create your views here.
def index(request):
    theIndex = open('static/index.html').read()
    return HttpResponse(theIndex)

@api_view(['GET'])
def get_grades(request):
    grades = Grade.objects.all()
    print(grades)
    data = serializers.serialize("json", grades, fields=['grade', 'student', 'assignment'])
    return HttpResponse(data)


@api_view(['GET'])
def get_assignments(request):
    assignments = Assignment.objects.all()
    print(assignments)
    data = serializers.serialize("json", assignments)
    return HttpResponse(data)

@api_view(['GET'])
def get_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    print(assignment)
    data = serializers.serialize("json", [assignment])
    return HttpResponse(data)