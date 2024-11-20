from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2', 'first_name', 'last_name']

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']