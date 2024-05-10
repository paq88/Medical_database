from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
# to jest paczka co pozwala pythonowi interpertować html

from django.http import HttpResponse
from sqlalchemy.testing.pickleable import User

from django.urls import path
from . import views  # Assuming your views.py is in the same app

def welcome_view(request):
    message = "<h1>Welcome to the users app</h1>"
    return HttpResponse(message)
def home(request):
    message = "<h1>Home page go to home page</h1>"
    return HttpResponse(message)
def rick(request, *args , **kwargs):
    return render(request,"base.html")

from .models import employes
from django.shortcuts import render

def list_users(request):
    all_employees = employes.objects.all()
    context = {'all_employees': all_employees}  # Create context dictionary
    return render(request, 'list_employees.html', context)

