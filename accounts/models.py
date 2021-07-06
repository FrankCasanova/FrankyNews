# django
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    """
    Custom user model 
    """
    age = models.PositiveIntegerField(null=True, blank=True)
