from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Handle profile image if needed
            if 'image_input' in request.FILES:
                profile_image = request.FILES['image_input']
                # Save the profile image in the appropriate place
                # For example, you might use a custom user profile model
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in after successful sign-up
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to a different page after successful sign-up
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('loggedin')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def loggedin(request):
    return render(request, 'loggedin.html')

def buy(request):
    return render(request, 'buy.html')

def post(request):
    return render(request, 'post.html')

def profile(request):
    return render(request, 'profile.html')

def bankdetails(request):
    return render(request, 'bankdetails.html')

def vieworders(request):
    return render(request, 'vieworders.html')

def logout(request):
    return render(request, 'home.html')