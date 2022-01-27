from rest_framework import serializers
from .models import Conversation, ConversationCompleted
from assets.serializers import AudioSerializer
from users.models import User
from courses.models import Unit, UnitCompleted
from quizzes.models import Quiz, QuizCompleted
from lessons.models import Lesson, LessonCompleted


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ConversationCompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConversationCompleted
        fields = ('__all__')

    # def create(self, request):
    #     data = request.data

    #     conversation = Conversation.objects.get(id=data['conversationId'])
    #     student = User.objects.get(username=data['username'])
    #     # print(quiz.title)
    #     # print(student.username)
    #     # quiz = Quiz.objects.get(id=1)
    #     # student = User.objects.get(username='sibiyan')
    #     unit = Unit.objects.get(pk=quiz.unit.id)

    #     ConversationCompleted_qs = UnitCompleted.objects.filter(
    #         student=student, is_completed=True, unit=unit)
    #     if not len(unitCompleted_qs) > 0:
    #         lessons_in_unit = Lesson.objects.filter(unit=unit)
    #         completed_lessons = LessonCompleted.objects.filter(
    #             student=student, is_completed=True, lesson__unit=unit)

    #         quizzes_in_unit = Quiz.objects.filter(unit=unit)
    #         completed_quizzes = QuizCompleted.objects.filter(
    #             student=student, is_completed=True, quiz__unit=unit).distinct()

    #         total_items = len(lessons_in_unit) + len(quizzes_in_unit)
    #         total_completed_items = len(
    #             completed_lessons) + len(completed_quizzes) + 1

    #         if total_completed_items >= total_items:
    #             print("all completed from quiz complete create")
    #             unitCompleted = UnitCompleted.objects.create(
    #                 student=student,
    #                 unit=unit,
    #                 is_completed=True
    #             )
    #             unitCompleted.save()
    #     quizCompleted_qs = QuizCompleted.objects.filter(
    #         student=student, is_completed=True, quiz=quiz)
    #     if not len(quizCompleted_qs) > 0:
    #         QuizCompleted = QuizCompleted()
    #         QuizCompleted.quiz = quiz
    #         QuizCompleted.student = student
    #         QuizCompleted.is_completed = True
    #         QuizCompleted.save()
    #         return QuizCompleted
    #     return
    #     print("quiz already completed")


class ConversationSerializer(serializers.ModelSerializer):
    # quizCompleted = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'order', 'subtitle', 'unit']

    # def get_quizCompleted(self, obj):
    #     try:
    #         username = self.context['username']
    #         user = User.objects.get(username=username)
    #         userId = user.id
    #         quizCompleted = QuizCompletedSerializer(
    #             obj.QuizCompleted.filter(student=userId), many=True).data
    #         print(len(quizCompleted))
    #         if quizCompleted:
    #             if len(quizCompleted) > 0:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return False
    #     except:
    #         return False


class ConversationDetailSerializer(serializers.ModelSerializer):
    audio_1 = AudioSerializer(read_only=True)
    audio_2 = AudioSerializer(read_only=True)
    audio_3 = AudioSerializer(read_only=True)
    audio_4 = AudioSerializer(read_only=True)
    audio_5 = AudioSerializer(read_only=True)
    audio_6 = AudioSerializer(read_only=True)
    audio_7 = AudioSerializer(read_only=True)
    audio_8 = AudioSerializer(read_only=True)
    audio_9 = AudioSerializer(read_only=True)
    audio_10 = AudioSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = ('__all__')
