from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from course.models import City, Course, Group, Lesson, Semester, Subject
from course.serializer import (CitySerializer, CourseSerializer,
                               GroupSerializer, LearnSerializer,
                               LessonSerializer, ListCourseSerializer,
                               SemesterSerializer, SubjectSerializer)


class CityViewSet(ModelViewSet):
    queryset = City.objects.order_by('-id')
    serializer_class = CitySerializer


class SemesterViewSet(ModelViewSet):
    queryset = Semester.objects.order_by('-id')
    serializer_class = SemesterSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by('-id')
    serializer_class = GroupSerializer


class CourseViweSet(ModelViewSet):
    queryset = Course.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCourseSerializer
        return CourseSerializer


class LessonViewSet(ModelViewSet):

    queryset = Lesson.objects.order_by('-id')
    serializer_class = LessonSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.order_by('-id')
    serializer_class = SubjectSerializer


class Learn(APIView):
    serializer_class = LearnSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            fname = serializer.validated_data.get("fname")
            lname = serializer.validated_data.get("lname")
            fullname = fname + " " + lname
            return Response({"full_name": fullname},
                            status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
