# yourapp/backends.py

from django.contrib.auth.backends import BaseBackend
from .models import Users1  # Import your custom user model
from django.contrib.auth.hashers import check_password

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users1.objects.get(username=username)
            if user and check_password(password, user.password):
                return user
        except Users1.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Users1.objects.get(pk=user_id)
        except Users1.DoesNotExist:
            return None
