from django import forms
from .models import Plant, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'description', 'image', 'price', 'availability']

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
