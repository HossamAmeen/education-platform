from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    pass


class Admin(UserAccount):
    pass


class Manager(UserAccount):
    pass


class Teacher(UserAccount):
    pass


class Student(UserAccount):
    pass
