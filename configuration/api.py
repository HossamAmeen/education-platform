from rest_framework.viewsets import ModelViewSet


from configuration.models import Configuration, Slider, Review
from configuration.serializer import ConfigurationSerializer, SliderSerializer


class SliderViewSet(ModelViewSet):
    queryset = Slider.objects.order_by('ordering')
    serializer_class = SliderSerializer



class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.order_by('ordering')
    serializer_class = ReviewSerializer

class ConfigurationViewSet(ModelViewSet):
    queryset = Configuration.objects.order_by('-id')
    serializer_class = ConfigurationSerializer
 