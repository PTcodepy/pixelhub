
# pixelhub_app/urls.py

from django.urls import path
from .views.intro import intro   # Import the intro view from the views folder

urlpatterns = [
    path('', intro, name='intro'),
    # Add more paths as needed
]


