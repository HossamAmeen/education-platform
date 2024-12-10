from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    first_name = last_name = is_staff = date_joined = \
        is_superuser = groups = user_permissions = None

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class Admin(UserAccount):
    pass


class Manager(UserAccount):
    pass


class Teacher(UserAccount):
    address = models.CharField(max_length=100)


class Student(UserAccount):
    address = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=50)
