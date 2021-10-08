from rest_framework import serializers

from .models import UnitTest, Question, Choice, GradedUnitTest
from users.models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
    answer = StringSerializer(many=False)

    class Meta:
        model = Question
        # fields = ('id', 'choices', 'question', 'order')
        fields = '__all__'


class UnitTestSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = UnitTest
        fields = '__all__'

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions


class GradedUnitTestSerializer(serializers.ModelSerializer):
    # student = StringSerializer(many=False)

    class Meta:
        model = GradedUnitTest
        fields = ('__all__')

    def create(self, request):
        data = request.data
        # print(data)

        unit = UnitTest.objects.get(id=data['testID'])
        student = User.objects.get(username=data['username'])

        graded_utest = GradedUnitTest()
        graded_utest.nuit = unit
        graded_utest.student = student
        graded_utest.grade = data['score']
        graded_utest.save()
        return graded_utest
