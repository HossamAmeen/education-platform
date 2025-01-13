from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    first_name = last_name = is_staff = date_joined = \
        is_superuser = groups = user_permissions = None

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone']

    def get_role(self):
        if hasattr(self, 'admin'):
            return "admin"
        elif hasattr(self, 'manager'):
            return "manager"
        elif hasattr(self, 'teacher'):
            return "teacher"
        elif hasattr(self, 'student'):
            return "student"

    def __str__(self):
        return self.email


class Admin(UserAccount):
    pass


class Manager(UserAccount):
    pass


class Teacher(UserAccount):
    address = models.CharField(max_length=100)


class Student(UserAccount):
    address = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=50)
