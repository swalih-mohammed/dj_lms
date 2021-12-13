from rest_framework import serializers
from .models import Photo, Audio


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = '__all__'
