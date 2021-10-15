from rest_framework import serializers
from .models import Quiz, Question, TextChoices, PhotoChoices


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class TextChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextChoices
        fields = ('__all__')


class PhotoChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoChoices
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):
    text_choices = serializers.SerializerMethodField()
    photo_choices = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('__all__')

    def get_text_choices(self, obj):
        qs = TextChoiceSerializer(
            obj.text_choices.all(), many=True).data
        return qs

    def get_photo_choices(self, obj):
        qs = PhotoChoiceSerializer(
            obj.photo_choices.all(), many=True).data
        return qs


class QuizSerializer(serializers.ModelSerializer):
    # photo_choices = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = (['id'])


class QuizDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_questions(self, obj):
        qs = QuestionSerializer(
            obj.questionQuizzes.all(), many=True).data
        return qs
