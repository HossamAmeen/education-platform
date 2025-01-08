from rest_framework.viewsets import ModelViewSet

from course.models import City, Course, Group, Lesson, Semester, Subject
from course.serializer import (CitySerializer, CourseSerializer,
                               GroupSerializer, LessonSerializer,
                               ListCourseSerializer, SemesterSerializer,
                               SubjectSerializer)


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
