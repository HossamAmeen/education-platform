from rest_framework.routers import DefaultRouter

from configuration.api import ReviewViewSet, SliderViewSet

router = DefaultRouter()
router.register(r'sliders', SliderViewSet, basename="sliders")
router.register(r'reviews', ReviewViewSet, basename="reviews")
urlpatterns = router.urls
