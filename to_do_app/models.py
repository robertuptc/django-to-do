from django.db import models
from django.contrib.auth.models import (AbstractUser)


class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='todos')
