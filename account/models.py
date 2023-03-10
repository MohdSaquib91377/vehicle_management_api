from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from account import managers as account_manager
# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


    class Meta:
        abstract = True


class User(TimeStampedModel,AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USERNAME_FIELD="email"
    objects = account_manager.UserManager()
    REQUIRED_FIELDS = []


    class Meta:
        ordering = ("-created_at",)