from rest_framework.viewsets import ModelViewSet

from configuration.models import Slider
from configuration.serializer import SliderSerializer


class SliderViewSet(ModelViewSet):
    queryset = Slider.objects.order_by('ordering')
    serializer_class = SliderSerializer
