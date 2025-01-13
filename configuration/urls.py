from rest_framework.routers import DefaultRouter

from configuration.api import SliderViewSet

router = DefaultRouter()
router.register(r'sliders', SliderViewSet, basename="sliders")
urlpatterns = router.urls
