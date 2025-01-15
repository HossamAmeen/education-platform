from rest_framework import serializers


from configuration.models import Configuration, Slider, Review


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = '__all__'
