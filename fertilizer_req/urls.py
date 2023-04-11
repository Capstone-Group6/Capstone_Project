from django.urls import path
from . import views as fertilizer_views
from accounts import views as home_page


# URL patterns for the fertilizer requirement app
urlpatterns = [
    # path for the fertilizer requirement prediction view
    path('fertilizer_requirement/', fertilizer_views.fertilizer_req, name='fertilizer_requirement'),
    path('home/', home_page, name='home'),
]