from rest_framework.routers import DefaultRouter

from course.api import (CityViewSet, CourseViweSet, GroupViewSet,
                        LessonViewSet, SemesterViewSet, SubjectViewSet)

router = DefaultRouter()
router.register(r'cities', CityViewSet, basename="cities")
router.register(r'semesters', SemesterViewSet, basename="semesters")
router.register(r'groups', GroupViewSet, basename="groups")
router.register(r'courses', CourseViweSet, basename="courses")
router.register(r'lessons', LessonViewSet, basename="lessons")
router.register(r'subjects', SubjectViewSet, basename="subjects")
urlpatterns = router.urls
