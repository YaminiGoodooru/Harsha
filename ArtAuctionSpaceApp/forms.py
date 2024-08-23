from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
           'pid','cost', 'full_name', 'phone','email', 
            'street_address', 'zip', 'state', 'city',
            'quantity','card_number', 'cvv'
        ]


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    image_input = forms.ImageField(required=False)  # Handle profile image

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data
