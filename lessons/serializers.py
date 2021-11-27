from rest_framework import serializers

from .models import Lesson, LessonItem, LessonCompleted
from users.models import User
from .models import User
from quizzes.serializers import QuizSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class LessonCompletedSerializer(serializers.ModelSerializer):

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


class LessonItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonItem
        fields = ('__all__')


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
        try:
            username = self.context['username']
            user = User.objects.get(username=username)
            userId = user.id

            lessonCompleted = LessonCompletedSerializer(
                obj.lessonCompleted.filter(student=userId), many=True).data
            if lessonCompleted:
                if len(lessonCompleted) > 0:
                    return True
                return False
        except:
            return False

    # def get_user(self, request):
    #     re = request.data
    #     print(re)
    #     return


class LessonDetailSerializer(serializers.ModelSerializer):
    Lesson_items = serializers.SerializerMethodField()
    quiz = serializers.SerializerMethodField()
    language1 = serializers.CharField(
        read_only=True, source="section.course.language.title")
    language2 = serializers.CharField(
        read_only=True, source="unit.section.course.language.title")

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_Lesson_items(self, obj):
        lessonItems = LessonItemSerializer(
            obj.LessonItems.all(), many=True).data
        return lessonItems

    def get_quiz(self, obj):
        lessonItems = QuizSerializer(
            obj.lessonQuizzes.all(), many=True).data
        return lessonItems
