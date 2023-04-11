from django.urls import path
from . import views as crop_yield_views
from accounts import views as home_page

urlpatterns = [
    # Define URL pattern for the crop_yield_prediction view function
    path('crop_yield_prediction/', crop_yield_views.crop_yield_prediction, name='crop_yield_prediction'),
    path('home/', home_page, name='home')
]
