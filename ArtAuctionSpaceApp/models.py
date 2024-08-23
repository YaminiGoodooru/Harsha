from django.db import models
from django.contrib.auth.models import User

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
    email = models.EmailField(default='example@example.com')  # Default email value
    artname = models.CharField(max_length=100, default='Unknown Art')  # Default art name
    artistname = models.CharField(max_length=255, default='Unknown Artist')  # Default artist name
    materials = models.TextField(default='Unknown materials')  # Default materials
    mobileno = models.CharField(max_length=15, default='0000000000')  # Default mobile number
    upi_id = models.CharField(max_length=50, default='example@upi')  # Default UPI ID
    price = models.IntegerField(default=0)  # Default price
    description = models.TextField(default='No description')  # Default description
    image = models.ImageField(upload_to='art_images/', default='art_images/default.jpg')  # Default image path

    def __str__(self):
        return self.artname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
