# pixelhub_app/views/intro.py

from django.shortcuts import render

def intro(request):
    return render(request, 'intro.html')
