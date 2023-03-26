# Import the path function from the django.urls module
from django.urls import path

# Import the crop_recommend view from the recommendation_views module
from . import views as recommendation_views


# Define a URL pattern that maps the URL "/crop_recommend/" to the crop_recommend view
urlpatterns = [
    path('crop_recommend/', recommendation_views.crop_recommend, name='crop_recommend')
]
