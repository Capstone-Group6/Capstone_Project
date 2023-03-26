from django.urls import path
from . import views as fertilizer_views


# URL patterns for the fertilizer requirement app
urlpatterns = [
    # path for the fertilizer requirement prediction view
    path('fertilizer_requirement/', fertilizer_views.fertilizer_requirement, name='fertilizer_requirement'),
]