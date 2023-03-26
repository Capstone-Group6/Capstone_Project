from django.urls import path
from . import views as crop_yield_views


urlpatterns = [
    # Define URL pattern for the crop_yield_prediction view function
    path('crop_yield_prediction/', crop_yield_views.crop_yield_prediction, name='crop_yield_prediction'),
]
