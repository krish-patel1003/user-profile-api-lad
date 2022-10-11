from decimal import DefaultContext
from enum import unique
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserProfileManager
# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a user profile inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Use to get a users full name """
        return f'{self.name}'

    def get_short_name(self):
        """ Used to get user's short name"""
        return f'{self.name}'

    def __str__(self):
        return f'{self.get_full_name} - {self.email}'