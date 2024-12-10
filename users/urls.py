from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, ManagerViewSet, StudentViewSet,
                       TeacherViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'teachers', TeacherViewSet, basename="teachers")
router.register(r'students', StudentViewSet, basename="students")
router.register(r'managers', ManagerViewSet, basename="managers")
urlpatterns = router.urls
