from django.shortcuts import redirect, render

from django.http import HttpResponse

# Create your views here.

# basic homepage
def home(request):
  return HttpResponse('<h1>Welcome to Frizzy!</h1>')