from rest_framework.routers import DefaultRouter

from configuration.api import ConfigurationViewSet, SliderViewSet

router = DefaultRouter()
router.register(r'sliders', SliderViewSet, basename="sliders")
router.register(r'configuration',
                ConfigurationViewSet, basename='configuration')
urlpatterns = router.urls
