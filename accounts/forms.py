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
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
