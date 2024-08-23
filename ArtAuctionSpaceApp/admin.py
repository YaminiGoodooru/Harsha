from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import Order,Paintings

# Optionally, unregister the default User admin
admin.site.unregister(User)

# Define a custom User admin
class UserAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ()

    # Use the default UserCreationForm and UserChangeForm
    add_form = UserCreationForm
    form = UserChangeForm

# Register the custom User admin
admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(Paintings)