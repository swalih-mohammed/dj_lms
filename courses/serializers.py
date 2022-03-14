from rest_framework import serializers
from users.models import User
from .models import Course, EnrolledCourse, Section, Unit, UnitCompleted
from lessons.models import Lesson, LessonCompleted
from quizzes.models import Quiz, QuizCompleted
from conversations.models import Conversation, ConversationCompleted

from lessons.serializers import LessonSerializer, LessonCompletedSerializer
from quizzes.serializers import QuizSerializer, QuizCompletedSerializer
from conversations.serializers import ConversationSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'


class SectionDetailSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_units(self, obj):
        units = UnitSerializer(obj.Units.all(), many=True).data
        return units

    def get_lessons(self, obj):
        lessons = LessonSerializer(obj.Sections.all(), many=True).data
        return lessons


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['id', 'title', 'subtitle', 'photo', 'language']


class EnrolledCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    completed_units = serializers.SerializerMethodField()
    total_units = serializers.SerializerMethodField()

    class Meta:
        model = EnrolledCourse
        fields = '__all__'

    def create(self, request):
        data = request.data
        course = Course.objects.get(id=data['courseId'])
        student = User.objects.get(username=data['username'])
        # course = Course.objects.get(id=1)
        # student = User.objects.get(username='sibiyan')

        courseEnrolled_qs = EnrolledCourse.objects.filter(
            student=student, course=course)

        if not len(courseEnrolled_qs) > 0:
            courseEnrolled = EnrolledCourse()
            courseEnrolled.course = course
            courseEnrolled.student = student
            courseEnrolled.is_enrolled = True
            courseEnrolled.save()
            print("creating new enrolled course")
            return courseEnrolled
        if courseEnrolled_qs[0].is_enrolled == False:
            print("enolled but unenrolled")
            courseEnrolled_qs[0].is_enrolled = True
            courseEnrolled_qs[0].save()
            return
        else:
            print("else in enrollling to course")
            courseEnrolled_qs[0].is_enrolled = False
            courseEnrolled_qs[0].save()
            return

    def get_completed_units(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        student = User.objects.get(username=username)

        completed_units = UnitCompleted.objects.filter(
            student=student, is_completed=True, unit__course=obj.course.id).distinct()
        return len(completed_units)

    def get_total_units(self, obj):
        units = Unit.objects.filter(
            course=obj.course.id)
        return len(units)


class CourseDetailSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()
    total_units = serializers.SerializerMethodField()
    completed_units = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_units(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        units = UnitSerializer(
            obj.Units.all(), many=True, context={'username': username}).data
        return units

    def get_completed_units(self, obj):
        try:
            request = self.context['request']
            username = request.parser_context['kwargs']['username']
            user = User.objects.get(username=username)
            completed_units = UnitCompleted.objects.filter(
                student=user.id, is_completed=True, unit__course=obj.id).distinct()
            return len(completed_units)
        except:
            print("error in finding progress")
            return 0

    def get_total_units(self, obj):
        units_in_course = obj.Units.all()
        return len(units_in_course)

    def get_is_enrolled(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        user = User.objects.get(username=username)
        enrolledCourse_qs = EnrolledCourse.objects.filter(
            student=user, is_enrolled=True, course=obj.id).distinct()
        if len(enrolledCourse_qs) > 0:
            return True
        else:
            return False


class UnitSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_progress(self, obj):
        try:
            username = self.context['username']
            user = User.objects.get(username=username)

            # lessons in unit
            lessons_in_unit = obj.Lessons.all()
            completed_lessons = LessonCompleted.objects.filter(
                student=user.id, is_completed=True, lesson__unit=obj.id).distinct()

            # quizzes in unit
            quizzes_in_unit = obj.unitQuizzes.all()
            completed_quizzes = QuizCompleted.objects.filter(
                student=user.id, is_completed=True, quiz__unit=obj.id).distinct()

            # conversations in unit
            conversation_in_unit = obj.conversations.all()
            completed_conversations = ConversationCompleted.objects.filter(
                student=user.id, is_completed=True, conversation__unit=obj.id)

            print("total", conversation_in_unit)
            # calcualte total progress of unit
            total_itmes = len(lessons_in_unit) + \
                len(quizzes_in_unit)+len(conversation_in_unit)
            total_completed_items = len(
                completed_lessons)+len(completed_quizzes)+len(completed_conversations)

            if total_itmes == 0 or total_completed_items == 0:
                return 0
            progress = total_completed_items/total_itmes
            return progress

        except:
            print("error in finding progress")
            return 0


class UnitDetailSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    quizzes = serializers.SerializerMethodField()
    conversations = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_lessons(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        lessons = LessonSerializer(
            obj.Lessons.all(), many=True, context={'username': username}).data
        return lessons

    def get_quizzes(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        quizzes = QuizSerializer(obj.unitQuizzes.all(), many=True, context={
            'username': username}).data
        return quizzes

    def get_conversations(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        conversations = ConversationSerializer(obj.conversations.all(), many=True, context={
            'username': username}).data
        return conversations
