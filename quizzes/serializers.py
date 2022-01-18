from rest_framework import serializers
from .models import Quiz, QuizCompleted, Question, TextChoices, PhotoChoices, QuestionType
from assets.serializers import PhotoSerializer, AudioSerializer
from users.models import User


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

        quiz_completed = QuizCompleted()
        quiz_completed.quiz = lesson
        quiz_completed.student = student
        quiz_completed.is_completed = True
        quiz_completed.save()
        return quiz_completed


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
            print(len(quizCompleted))
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

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_questions(self, obj):
        qs = QuestionSerializer(
            obj.quizzes.all(), many=True).data
        return qs
