from unicodedata import category
from rest_framework import serializers
from .models import Quiz, QuizCompleted, Question
from assets.serializers import PhotoSerializer, AudioSerializer
from users.models import User
from courses.models import Unit, UnitCompleted, EnrolledCourse, Course
from quizzes.models import Quiz, QuizCompleted
from lessons.models import Lesson, LessonCompleted


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
        quiz = Quiz.objects.get(id=data['quiz_id'])
        student = User.objects.get(id=data['user_id'])
        score = data['score']

        if quiz.unit != None:
            unit = Unit.objects.get(pk=quiz.unit.id)
            # course = Course.objects.get(pk=unit.course.id)
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
                print("totla itmes", total_completed_items)
                if total_completed_items >= total_items:
                    print("making unit complete")
                    unitCompleted = UnitCompleted.objects.create(
                        student=student,
                        unit=unit,
                        is_completed=True
                    )
                    unitCompleted.save()

        quizCompleted_qs = QuizCompleted.objects.filter(
            student=student, quiz=quiz)
        if not len(quizCompleted_qs) > 0:
            print("quiz complete created")
            quizCompleted = QuizCompleted()
            quizCompleted.quiz = quiz
            quizCompleted.student = student
            quizCompleted.score = score
            quizCompleted.is_completed = True
            quizCompleted.save()
            return
        else:  # quiz exist but not completed
            quizCompleted_qs[0].is_completed = True
            quizCompleted_qs[0].score = score
            quizCompleted_qs[0].save()
            print("quiz is complete updated")
            return


class QuizSerializer(serializers.ModelSerializer):
    quizCompleted = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_quizCompleted(self, obj):
        try:
            user_id = self.context['user_id']
            user = User.objects.get(id=user_id)
            quizCompleted = QuizCompletedSerializer(
                obj.QuizCompleted.filter(student=user), many=True).data
            if quizCompleted:
                if len(quizCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


class GeneralQuizListSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('__all__')

    def get_score(self, obj):
        try:
            request = self.context['request']
            user_id = request.parser_context['kwargs']['user_id']
            user = User.objects.get(id=user_id)
            category = request.parser_context['kwargs']['category']
            qs = obj.QuizCompleted.filter(
                student=user, quiz__category=category)
            score = qs[0].score
            return score
        except:
            return 0


class QuizDetailSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(read_only=True)
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
            username = request.parser_context['kwargs']['user_id']
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
