from rest_framework import serializers

from .models import Section
from units.serializers import UnitSerializer, UnitDetailSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class SectionSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_units(self, obj):
        units = UnitSerializer(obj.units.all(), many=True).data
        return units
