from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CreditCard, Order

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=254,
        help_text="Enter an email address to receive digital receipts and promotion offers."
    )
    address = forms.CharField(
        max_length=200,
        help_text="Your address information is used to provide delivery services.",
    )
    phone_number = forms.CharField(
        max_length=11,
        help_text="Your phone number allows drivers to contact you if needed.",
    )

    class Meta:
        model = User
        fields = {
            'username', 
            'password1', 
            'password2', 
            'first_name', 
            'last_name', 
            'email', 
            'address', 
            'phone_number'
        }
    
    field_order = [
        'username', 
        'password1', 
        'password2', 
        'first_name', 
        'last_name', 
        'email', 
        'address', 
        'phone_number'
    ]
 
class CreditCardForm(ModelForm):
  class Meta:
    model = CreditCard
    fields = ['card_number', 'security_code', 'exp_date']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'shop', 'creditcard', 'icecreams']