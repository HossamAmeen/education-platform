from django.urls import path

from auth.api import LoginAPI, RegisterUserAccountAPI

urlpatterns = [
    path('register/', RegisterUserAccountAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]
