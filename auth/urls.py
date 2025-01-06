from django.urls import path

from auth.api import RegisterUserAccountAPI

urlpatterns = [
    path('register/', RegisterUserAccountAPI.as_view(), name='register')
]
