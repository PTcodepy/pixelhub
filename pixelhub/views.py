# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def home(request):
    return HttpResponse("Hello, this is the home view!")

def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

def intro(request):
    template = get_template('teste.html')
    return render(request, template)