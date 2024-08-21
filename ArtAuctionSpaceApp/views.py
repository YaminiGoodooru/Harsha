from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .models import Users1
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        useremail = request.POST.get('useremail')  # Retrieve the email from the form

        if not Users1.objects.filter(username=username).exists():
            # Manually hash the password and create the user
            hashed_password = make_password(password)
            user = Users1(username=username, password=hashed_password, useremail=useremail)
            user.save()  # Save the user to the database

            messages.success(request, 'User created successfully')
            return redirect('login')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Username already exists')

    return render(request, 'signup.html')
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user is valid, log them in
            login(request, user)
            messages.success(request, f'Welcome, {username}! You have been logged in.')
            return redirect('home')  # Redirect to the home page or any other page after successful login
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
def about(request):
    return render(request, 'about.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')
