
from rest_framework import serializers
from .models import Bug


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'
        # fields = ['nickName', 'photo', ]
