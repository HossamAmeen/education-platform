from rest_framework.routers import DefaultRouter

from configuration.api import ReviewViewSet, SliderViewSet, ConfigurationViewSet

router = DefaultRouter()
router.register(r'sliders', SliderViewSet, basename="sliders")
router.register(r'reviews', ReviewViewSet, basename="reviews")
router.register(r'configuration',
                ConfigurationViewSet, basename='configuration')

urlpatterns = router.urls
