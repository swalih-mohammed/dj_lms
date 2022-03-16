from rest_framework import serializers
from .models import Quiz, QuizCompleted, Question, TextChoices, PhotoChoices, QuestionType
from assets.serializers import PhotoSerializer, AudioSerializer
from users.models import User
from courses.models import Unit, UnitCompleted
from quizzes.models import Quiz, QuizCompleted
from lessons.models import Lesson, LessonCompleted


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class TextChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextChoices
        fields = ('__all__')


class PhotoChoiceSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = PhotoChoices
        fields = ('__all__')


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('__all__')


class QuestionSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(read_only=True)
    photo_option_1 = PhotoSerializer(read_only=True)
    photo_option_2 = PhotoSerializer(read_only=True)
    photo_option_3 = PhotoSerializer(read_only=True)
    photo_option_4 = PhotoSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('__all__')


class QuizCompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizCompleted
        fields = ('__all__')

    def create(self, request):
        data = request.data

        quiz = Quiz.objects.get(id=data['quizId'])
        student = User.objects.get(username=data['username'])
        # print(quiz.title)
        # print(student.username)
        # quiz = Quiz.objects.get(id=1)
        # student = User.objects.get(username='sibiyan')
        unit = Unit.objects.get(pk=quiz.unit.id)
        # print(data)
        # print(student.username)
        # print(quiz.title)
        # print(unit.title)

        unitCompleted_qs = UnitCompleted.objects.filter(
            student=student, is_completed=True, unit=unit)
        if not len(unitCompleted_qs) > 0:
            lessons_in_unit = Lesson.objects.filter(unit=unit)
            completed_lessons = LessonCompleted.objects.filter(
                student=student, is_completed=True, lesson__unit=unit)

            quizzes_in_unit = Quiz.objects.filter(unit=unit)
            completed_quizzes = QuizCompleted.objects.filter(
                student=student, is_completed=True, quiz__unit=unit).distinct()

            total_items = len(lessons_in_unit) + len(quizzes_in_unit)
            total_completed_items = len(
                completed_lessons) + len(completed_quizzes) + 1

            if total_completed_items >= total_items:
                print("all completed from quiz complete create")
                unitCompleted = UnitCompleted.objects.create(
                    student=student,
                    unit=unit,
                    is_completed=True
                )
                unitCompleted.save()
        quizCompleted_qs = QuizCompleted.objects.filter(
            student=student, quiz=quiz)
        if not len(quizCompleted_qs) > 0:
            quizCompleted = QuizCompleted()
            quizCompleted.quiz = quiz
            quizCompleted.student = student
            quizCompleted.is_completed = True
            quizCompleted.save()
            return
        if quizCompleted_qs[0].is_completed == False:  # quiz exist but not completed
            quizCompleted_qs[0].is_completed == True
            quizCompleted_qs[0].save()
            return
        print("quiz already completed")
        return


class QuizSerializer(serializers.ModelSerializer):
    quizCompleted = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_quizCompleted(self, obj):
        try:
            username = self.context['username']
            user = User.objects.get(username=username)
            userId = user.id
            quizCompleted = QuizCompletedSerializer(
                obj.QuizCompleted.filter(student=userId), many=True).data
            # print(len(quizCompleted))
            if quizCompleted:
                if len(quizCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


class QuizDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_questions(self, obj):
        qs = QuestionSerializer(
            obj.quizzes.all(), many=True).data
        return qs

    def get_is_completed(self, obj):
        try:
            request = self.context['request']
            username = request.parser_context['kwargs']['username']
            # username = self.context['username']
            user = User.objects.get(username=username)
            userId = user.id
            quizCompleted = QuizCompletedSerializer(
                obj.QuizCompleted.filter(student=userId), many=True).data
            # print("user from quiz completed", user)
            if quizCompleted:
                if len(quizCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
