from rest_framework.viewsets import ModelViewSet

from configuration.models import Review, Slider
from configuration.serializer import ReviewSerializer, SliderSerializer


class SliderViewSet(ModelViewSet):
    queryset = Slider.objects.order_by('ordering')
    serializer_class = SliderSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.order_by('ordering')
    serializer_class = ReviewSerializer
