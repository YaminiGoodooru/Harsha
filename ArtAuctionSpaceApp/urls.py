from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('about/',views.about,name='about'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('loggedin/',views.loggedin,name='loggedin'),
    path('bankdetails/',views.bankdetails,name='bankdetails'),
    path('post/',views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('buy/',views.buy,name='buy'),
    path('vieworders/',views.vieworders,name='vieworders'),
    path('logout/',views.logout,name='logout'),
    path('editprofile/', views.editprofile, name='editprofile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
