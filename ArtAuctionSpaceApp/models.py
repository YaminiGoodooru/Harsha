from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Order(models.Model):
    pid = models.IntegerField()
    cost=models.IntegerField()
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    street_address = models.CharField(max_length=255)
    zip = models.IntegerField(max_length=10)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    card_number = models.IntegerField(max_length=16)
    cvv = models.IntegerField(max_length=4)

    def __str__(self):
        return f"Order by {self.full_name}"


class Paintings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    email = models.EmailField()  # Removed default value
    pid=models.IntegerField(default=0)
    artname = models.CharField(max_length=100)  # Removed default value
    artistname = models.CharField(max_length=255)  # Removed default value
    materials = models.TextField()  # Removed default value
    mobileno = models.CharField(max_length=15)  # Removed default value
    upi_id = models.CharField(max_length=50)  # Removed default value
    price = models.IntegerField()  # Removed default value
    description = models.TextField()  # Removed default value
    image = models.ImageField(upload_to='paintings/')  # Removed default value

    def __str__(self):
        return self.artname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
