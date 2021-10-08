from rest_framework import serializers

from .models import Lesson, LessonQuestion, LessonQuestionChoice, LessonCompleted
from users.models import User
# from films.serializers import FilmSerializer
# from unitTests.serializers import UnitTestSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class LessonQuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)

    class Meta:
        model = LessonQuestion
        fields = '__all__'


class LessonCompletedSerializer(serializers.ModelSerializer):
    # student = StringSerializer(many=False)

    class Meta:
        model = LessonCompleted
        fields = ('__all__')

    def create(self, request):
        data = request.data
        # print(data)

        lesson = Lesson.objects.get(id=data['lessonId'])
        student = User.objects.get(username=data['username'])

        lesson_completed = LessonCompleted()
        lesson_completed.lesson = lesson
        lesson_completed.student = student
        lesson_completed.is_completed = True
        lesson_completed.save()
        return lesson_completed


class LessonSerializer(serializers.ModelSerializer):
    lessonCompleted = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField()
    # field3 = serializers.SerializerMethodField('get_filtered_data')

    # def get_filtered_data(self, obj):
    #     param_value = self.context['request'].QUERY_PARAMS.get(
    #         'username', None)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_lessonCompleted(self, obj):
        username = self.context['username']
        user = User.objects.get(username=username)
        userId = user.id

        lessonCompleted = LessonCompletedSerializer(
            obj.lessonCompleted.filter(student=userId), many=True).data
        if lessonCompleted:
            if len(lessonCompleted) > 0:
                return True
        return False

    def get_user(self, request):
        re = request.data
        print(re)
        return


class LessonDetailSerializer(serializers.ModelSerializer):
    lessonQuestions = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_lessonQuestions(self, obj):
        lessons = LessonQuestionSerializer(
            obj.lessonsQuestions.all(), many=True).data
        return lessons
