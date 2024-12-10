from rest_framework import serializers

from users.models import Admin, Manager, Student, Teacher


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'username', 'is_active',
                  'full_name', 'phone', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ['id', 'username', 'is_active',
                  'full_name', 'phone', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'username', 'is_active', 'address',
                  'full_name', 'phone', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'username', 'is_active', 'parent_phone', 'address',
                  'full_name', 'phone', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
