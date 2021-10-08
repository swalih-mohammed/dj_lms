from rest_framework import serializers

from .models import Course
from sections.serializers import SectionSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_sections(self, obj):
        sections = SectionSerializer(obj.sections.all(), many=True).data
        return sections
