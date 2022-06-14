from django.contrib.auth.forms import UserCreationForm  
from .models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2','email','is_admin','is_volunteer','is_coordinator']

class LoginForm(forms.Form):
    username =forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    ) 
    password =forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    ) 

    