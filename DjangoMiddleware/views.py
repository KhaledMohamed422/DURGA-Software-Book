from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    print(10/0) 
    return HttpResponse('<h1>Hello This is from home page view</h1>')

def welcome_view(request):
    print('This line added by view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')



