from django.db import models


# Define a User model
class User(models.Model):
    # Define fields for the model
    username = models.CharField(max_length=100) # CharField for username with a maximum length of 100 characters
    email = models.EmailField(max_length=100) # EmailField for email with a maximum length of 100 characters
    password = models.CharField(max_length=15) # CharField for password with a maximum length of 15 characters

    # other field to be added according to need

