from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
# Create your views here.

def get_persons(request):
    persons = Person.objects.all()
    return JsonResponse({'name':'Ali'})
    