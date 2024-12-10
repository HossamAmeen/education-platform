from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Admin, Manager, Student, Teacher
from users.serializers import (AdminSerializer, ManagerSerializer,
                               StudentSerializer, TeacherSerializer)


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.order_by('-id')
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.order_by('-id')
    serializer_class = ManagerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']
