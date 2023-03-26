# Importing forms and User model from models.py
from django import forms
from .models import User


# Defining UserForm class which is a subclass of ModelForm
class UserForm(forms.ModelForm):
    # Setting the input type of password field as PasswordInput
    password = forms.CharField(widget=forms.PasswordInput)

    # Setting the model for this form and the fields to be displayed
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# Defining LoginForm class which is a subclass of Form
class LoginForm(forms.Form):
    # Setting the max length of username field
    username = forms.CharField(max_length=100)
    # Setting the input type of password field as PasswordInput
    password = forms.CharField(widget=forms.PasswordInput)
