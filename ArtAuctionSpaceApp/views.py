from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .forms import SignUpForm,PaintingsForm,OrderForm,ProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Paintings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Order

def vieworders(request):
    # Assuming 'Orders' is the model and it has a foreign key to the user or a buyer field
    orderdetails = Order.objects.filter(email=request.user.email)
    return render(request, 'vieworders.html', {'orderdetails': orderdetails})
def profile(request):
    # Get the current logged-in user
    user = request.user
    # Pass the user details to the template
    return render(request, 'profile.html', {
        'username': user.username,
        'email': user.email,
    })

def buy(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buy')  # Redirect to a success page or another view
    else:
        form = OrderForm()
    
    return render(request, 'buy.html', {'form': form})

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
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loggedin')  # Redirect to home or any other page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')



def loggedin(request):
    return render(request,'loggedin.html')

def post(request):
    if request.method == 'POST':
        form = PaintingsForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()  # Save form data to the database
            return redirect('post')  # Redirect to a success page or another view
    else:
        form = PaintingsForm()

    return render(request, 'post.html', {'form': form})

def bankdetails(request):
    return render(request, 'bankdetails.html')

def logout(request):
    return render(request, 'home.html')

def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')  # Redirect to profile page or another page
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'editprofile.html', {'form': form})