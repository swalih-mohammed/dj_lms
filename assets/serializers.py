from rest_framework import serializers
from .models import Photo, Voice, Audio, Video
# from assets.serializers import VoiceSerializer


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class VoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voice
        # fields = '__all__'
        fields = ['nickName', 'photo', ]


class AudioSerializer(serializers.ModelSerializer):
    voice = VoiceSerializer(read_only=True)

    class Meta:
        model = Audio
        # fields = '__all__'
        fields = ['audio',  'text', 'voice']


class VideoSerializer(serializers.ModelSerializer):
    voice = serializers.StringRelatedField()

    class Meta:
        model = Video
        fields = '__all__'
        # fields = ['audio', 'voice', 'text']
