# Import the admin module and the User model from the app models.py file
from django.contrib import admin
from .models import User


# Define the admin model for the User model with a custom display
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')


# Register the User model and the custom UserAdmin model with the Django admin site
admin.site.register(User, UserAdmin)