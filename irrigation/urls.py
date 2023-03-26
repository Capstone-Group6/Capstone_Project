# Importing the required modules
from django.urls import path
from . import views as irrigation_views


# Defining the URL patterns for the Irrigation app
urlpatterns = [
    # Mapping the URL to the view function 'irrigation_planning' inside the views.py module
    path('irrigation_planning/', irrigation_views.irrigation_planning, name='irrigation_planning'),
]