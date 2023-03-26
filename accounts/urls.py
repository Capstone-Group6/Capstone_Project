from django.urls import path
from .views import signup_page, login_page, home_page

# Define the URL patterns for the app
urlpatterns = [
    # When the user visits the root URL, redirect them to the login page
    path('', login_page, name='login'),
    # When the user visits the 'signup/' URL, show them the signup page
    path('signup/', signup_page, name='signup'),
]