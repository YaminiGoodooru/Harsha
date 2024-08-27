from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .forms import SignUpForm,PaintingsForm,OrderForm,ProfileForm,ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Paintings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from .forms import ForgotPasswordForm,ResetPasswordForm
from django.core.mail import send_mail
#User = get_user_model()
import random
import string

def forgotpassword(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            # Save the OTP and email to the session or database for verification later
            request.session['otp'] = otp
            request.session['email'] = email
            # Send email with the OTP
            send_mail(
                'Password Reset Request',
                f'Your OTP is: {otp}',
                'from@example.com',  # Replace with your email address
                [email],
                fail_silently=False,
            )
            messages.success(request, 'A password reset email has been sent.')
            return redirect('resetpassword')  # Redirect to a page where the user can enter the OTP
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgotpassword.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']
            if otp == request.session.get('otp'):
                email = request.session.get('email')
                # Here you should reset the password for the user with this email
                # This depends on your user model and how you handle passwords
                # For example, you might use Django's built-in user model:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been reset successfully.')
                return redirect('login')  # Redirect to the login page after resetting the password
            else:
                messages.error(request, 'Invalid OTP.')
    else:
        form = ResetPasswordForm()
    return render(request, 'resetpassword.html', {'form': form})


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

def posts(request):
    user_paintings = Paintings.objects.filter(user=request.user)
    context = {
        'userposts': {
            'paintings': user_paintings
        }
    }
    return render(request, 'posts.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=email,
                recipient_list=['yaminig3006@gmail.com'],  # Your email address
                fail_silently=False,
            )

            return redirect('contact')  # Redirect to a success page or wherever you like
    else:
        form = ContactForm()
    return render(request,'contact.html')