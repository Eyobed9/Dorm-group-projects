from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'user_choice', 'date_of_birth', 'phone', 'bio', 'image')

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')  
          # order of fields in form
