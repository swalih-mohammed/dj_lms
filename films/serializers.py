from rest_framework import serializers

from .models import Film


class FilmSerializer(serializers.ModelSerializer):
    # category = serializers.ReadOnlyField(source='shop_category.name')
    class Meta:
        model = Film
        fields = '__all__'
