from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from django.utils.crypto import get_random_string
from datetime import timedelta

# Create your models here.


class Manager(BaseUserManager):

    def create_superuser(self, email, username, password, name, surname, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, username, password, name, surname, **other_fields)

    def create_user(self, email, username, password, name, surname, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, surname=surname, **other_fields)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=80, unique=True)

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone = models.CharField(max_length=15, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = Manager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'name', 'surname']

    def __str__(self):
        return self.username

