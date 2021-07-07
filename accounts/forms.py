# django
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# models
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Thats work in order to adapt forms to our CustomUser
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):
    """
    Necessary class for always that the users wants change their fields
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')
