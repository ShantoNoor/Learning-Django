from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def index2(request):
    my_dict = {'insert_me': 'heoool from vies.py'}
    return render(request, 'first_app/index.html', context=my_dict)