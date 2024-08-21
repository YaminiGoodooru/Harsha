from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword')
]
