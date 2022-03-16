from assets.serializers import PhotoSerializer, AudioSerializer, VideoSerializer
from quizzes.serializers import QuizSerializer
from rest_framework import serializers

from .models import Lesson, LessonItem, LessonCompleted
from users.models import User
from courses.models import Unit, UnitCompleted
from quizzes.models import Quiz, QuizCompleted
# from .models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class LessonCompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonCompleted
        fields = ('__all__')

    def create(self, request):
        data = request.data

        lesson = Lesson.objects.get(id=data['lessonId'])
        student = User.objects.get(username=data['username'])

        # lesson = Lesson.objects.get(id=1)
        # student = User.objects.get(username='sibiyan')

        unit = Unit.objects.get(pk=lesson.unit.id)

        lessons_in_unit = Lesson.objects.filter(unit=lesson.unit)
        completed_lessons = LessonCompleted.objects.filter(
            student=student, is_completed=True, lesson__unit=lesson.unit)

        quizzes_in_unit = Quiz.objects.filter(unit=lesson.unit)
        completed_quizzes = QuizCompleted.objects.filter(
            student=student, is_completed=True, quiz__unit=lesson.unit).distinct()

        total_items = len(lessons_in_unit) + len(quizzes_in_unit)
        total_completed_items = len(
            completed_lessons) + len(completed_quizzes) + 1
        # print(unit.title)
        # print('total items', total_items)
        # print('total completed items', total_completed_items)

        if total_completed_items >= total_items:
            # print("all completed from lesson complete create")
            unitCompleted = UnitCompleted.objects.create(
                student=student,
                unit=unit,
                is_completed=True
            )
            unitCompleted.save()
        lesson_completed_qs = LessonCompleted.objects.filter(
            student=student, lesson=lesson)
        if not len(lesson_completed_qs) > 0:
            lesson_completed = LessonCompleted()
            lesson_completed.lesson = lesson
            lesson_completed.student = student
            lesson_completed.is_completed = True
            lesson_completed.save()
            return
        if lesson_completed_qs[0].is_completed == False:
            lesson_completed_qs[0].is_completed = True
            lesson_completed_qs[0].save()
            return
        return


class LessonItemSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    audio = AudioSerializer(read_only=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = LessonItem
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lessonCompleted = serializers.SerializerMethodField()

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
                # print("lesson completed")
                if len(lessonCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


class LessonDetailSerializer(serializers.ModelSerializer):
    Lesson_items = serializers.SerializerMethodField()
    quiz = serializers.SerializerMethodField()
    is_completed = serializers.SerializerMethodField()
    video = VideoSerializer(read_only=True)

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

    def get_is_completed(self, obj):
        try:
            request = self.context['request']
            username = request.parser_context['kwargs']['username']
            user = User.objects.get(username=username)
            userId = user.id

            lessonCompleted = LessonCompletedSerializer(
                obj.lessonCompleted.filter(student=userId), many=True).data
            if lessonCompleted:
                # print("lesson completed")
                if len(lessonCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
