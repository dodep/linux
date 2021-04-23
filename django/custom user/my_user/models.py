from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(max_length=1000, null=True)
    name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProxy(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True) 
    session = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        if not self.user:
            return self.session
        return self.user.email
