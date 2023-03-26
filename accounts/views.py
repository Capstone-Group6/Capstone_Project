from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Define a view that requires the user to be logged in to access it
@login_required(login_url='login')
def home_page(request):
    return render(request, 'home.html')


# Define a view for the signup page
def signup_page(request):
    if request.method == 'POST':  # If the request method is POST, process the form data
        uname = request.POST.get('username')  # Get the username from the form
        email = request.POST.get('email')  # Get the email from the form
        pass1 = request.POST.get('password1')  # Get the first password from the form
        pass2 = request.POST.get('password2')  # Get the second password from the form

        if pass1 != pass2:  # If the passwords don't match, return an error message
            return HttpResponse("Your password Mismatch!!")
        else: # Otherwise, create a new user and redirect to the login page
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')  # If the request method is GET, return the signup page


# Define a view for the login page
def login_page(request):
    if request.method == 'POST':  # If the request method is POST, process the form data
        username = request.POST.get('username')  # Get the username from the form
        pass1 = request.POST.get('pass')  # Get the password from the form
        user = authenticate(request, username=username, password=pass1)  # Authenticate the user

        if user is not None:  # If the user is authenticated, log them in and redirect to the home page
            login(request, user)
            return redirect('home')
        else:  # Otherwise, return an error message
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')  # If the request method is GET, return the login page


# Define a view for the logout page
def logout_page(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page
