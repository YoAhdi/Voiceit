from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.


def home(request) :
    return render(request, 'base/home.html')

def loginPage(request) :
    context = {}
    return render(request, 'base/login_register.html', context)