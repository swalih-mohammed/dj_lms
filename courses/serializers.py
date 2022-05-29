# from curses import flash
import datetime
import pytz
# from unicodedata import category
from rest_framework import serializers
from users.models import Student
from users.models import User
from .models import Course, CourseCategory, EnrolledCourse, Unit, UnitCompleted, LiveClass
from lessons.models import Lesson, LessonCompleted
from quizzes.models import Quiz, QuizCompleted
from conversations.models import Conversation, ConversationCompleted

from lessons.serializers import LessonSerializer, LessonCompletedSerializer
from quizzes.serializers import QuizSerializer, QuizCompletedSerializer
from conversations.serializers import ConversationSerializer


utc = pytz.UTC


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class LiveClassSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(
        source="teacher.username", read_only=True)
    class_date = serializers.DateTimeField(format="Date %d-%m-%Y Time %H:%M")

    class Meta:
        model = LiveClass
        fields = '__all__'


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    completed_units = serializers.SerializerMethodField()
    total_units = serializers.SerializerMethodField()
    current_level = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()
    start_date = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

# this is taking User, this has to be changed to student later on
    def get_completed_units(self, obj):
        request = self.context['request']
        user_id = request.parser_context['kwargs']['user_id']
        student = User.objects.get(pk=user_id)
        completed_units = UnitCompleted.objects.filter(
            student=student, is_completed=True, unit__course=obj.id).distinct()
        return len(completed_units)

    def get_total_units(self, obj):
        return len(obj.Units.all())

    def get_current_level(self, obj):
        request = self.context['request']
        user_id = request.parser_context['kwargs']['user_id']
        level = Student.objects.get(user=user_id).level
        return level

    # def get_current_level(self, obj):
    #     request = self.context['request']
    #     username = request.parser_context['kwargs']['id']
    #     student = Student.objects(user=username)
    #     return student

    # def get_current_level(self, obj):
    #     request = self.context['request']
    #     username = request.parser_context['kwargs']['username']
    #     student = User.objects.get(username=username)
    #     category = student.current_course
    #     level = student.level
    #     # category = request.parser_context['kwargs']['category']
    #     courses = Course.objects.filter(
    #         category=category).order_by('order')
    #     # level = 1
    #     for course in courses:
    #         total_units_in_course = course.Units.all()
    #         total_completed_units = UnitCompleted.objects.filter(
    #             student=student, is_completed=True, unit__course=obj.id)
    #         if len(total_units_in_course) == len(total_completed_units):
    #             level = level + 1
    #         else:
    #             break
    #     return level

    def get_is_enrolled(self, obj):
        # try:
        request = self.context['request']
        user_id = request.parser_context['kwargs']['user_id']
        user = User.objects.get(id=user_id)
        student = Student.objects.get(user=user)
        enrolledCourse_qs = EnrolledCourse.objects.filter(
            student=student, is_enrolled=True, course=obj.id)
        print(enrolledCourse_qs)
        if len(enrolledCourse_qs) > 0:
            end_date = enrolledCourse_qs.last().end_date.replace(tzinfo=utc)
            time_now = datetime.datetime.now().replace(tzinfo=utc)
            if end_date > time_now:
                return True
            else:
                return False
        else:
            return False
        # except:
        #     return False

    def get_start_date(self, obj):
        try:
            request = self.context['request']
            user_id = request.parser_context['kwargs']['user_id']
            user = User.objects.get(pk=user_id)
            student = Student.objects.get(user=user)
            enrolledCourse_qs = EnrolledCourse.objects.filter(
                student=student, is_enrolled=True, course=obj.id)
            if len(enrolledCourse_qs) > 0:
                start_date = enrolledCourse_qs.last().start_date
                start_date = start_date.strftime("%d-%m-%y")
                return start_date
        except:
            return None

    def get_end_date(self, obj):
        try:
            request = self.context['request']
            user_id = request.parser_context['kwargs']['user_id']
            user = User.objects.get(id=user_id)
            student = Student.objects.get(user=user)
            enrolledCourse_qs = EnrolledCourse.objects.filter(
                student=student, is_enrolled=True, course=obj.id)
            if len(enrolledCourse_qs) > 0:
                end_date = enrolledCourse_qs.last().end_date
                end_date = end_date.strftime("%d-%m-%y")
                return end_date
        except:
            return None


class EnrolledCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    completed_units = serializers.SerializerMethodField()
    total_units = serializers.SerializerMethodField()
    start_date = serializers.DateTimeField(format="%d-%m-%Y")
    end_date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = EnrolledCourse
        fields = '__all__'

    def create(self, request):
        data = request.data
        course = Course.objects.get(id=data['courseId'])
        student = User.objects.get(username=data['username'])
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
        user = User.objects.get(username=username)
        completed_units = UnitCompleted.objects.filter(
            student=user, is_completed=True, unit__course=obj.course.id).distinct()
        return len(completed_units)

    def get_total_units(self, obj):
        units = Unit.objects.filter(
            course=obj.course.id)
        return len(units)

    def get_is_enrolled(self, obj):
        try:
            print(self.end_date)

        except:
            return False


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
        user_id = request.parser_context['kwargs']['user_id']
        units = UnitSerializer(
            obj.Units.all(), many=True, context={'user_id': user_id}).data
        return units

    def get_completed_units(self, obj):
        try:
            request = self.context['request']
            user_id = request.parser_context['kwargs']['user_id']
            user = Student.objects.get(id=user_id)
            completed_units = UnitCompleted.objects.filter(
                student=user_id, is_completed=True, unit__course=obj.id).distinct()
            return len(completed_units)
        except:
            print("error in finding progress")
            return 0

    def get_total_units(self, obj):
        units_in_course = obj.Units.all()
        return len(units_in_course)

    def get_is_enrolled(self, obj):
        try:
            request = self.context['request']
            user_id = request.parser_context['kwargs']['user_id']
            user_id = User.objects.get(id=user_id)
            student = Student.objects.get(user=user_id)
            enrolledCourse_qs = EnrolledCourse.objects.filter(
                student=student, is_enrolled=True, course=obj.id)
            if len(enrolledCourse_qs) > 0:
                end_date = enrolledCourse_qs.last().end_date.replace(tzinfo=utc)
                time_now = datetime.datetime.now().replace(tzinfo=utc)
                if end_date > time_now:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


class UnitSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    liveClasses = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_liveClasses(self, obj):
        liveClasses = LiveClassSerializer(obj.units.all(), many=True).data
        return liveClasses

    def get_progress(self, obj):
        try:
            user_id = self.context['user_id']
            user = User.objects.get(id=user_id)
            lessons_in_unit = obj.Lessons.all()
            completed_lessons = LessonCompleted.objects.filter(
                student=user.id, is_completed=True, lesson__unit=obj.id).distinct()
            quizzes_in_unit = obj.unitQuizzes.all()
            completed_quizzes = QuizCompleted.objects.filter(
                student=user.id, is_completed=True, quiz__unit=obj.id).distinct()

            # conversations in unit
            conversation_in_unit = obj.conversations.all()
            completed_conversations = ConversationCompleted.objects.filter(
                student=user.id, is_completed=True, conversation__unit=obj.id)

            # print("total", conversation_in_unit)
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
        user_id = request.parser_context['kwargs']['user_id']
        lessons = LessonSerializer(
            obj.Lessons.all(), many=True, context={'user_id': user_id}).data
        return lessons

    def get_quizzes(self, obj):
        request = self.context['request']
        user_id = request.parser_context['kwargs']['user_id']
        quizzes = QuizSerializer(obj.unitQuizzes.all(), many=True, context={
            'user_id': user_id}).data
        return quizzes

    def get_conversations(self, obj):
        request = self.context['request']
        user_id = request.parser_context['kwargs']['user_id']
        conversations = ConversationSerializer(obj.conversations.all(), many=True, context={
            'user_id': user_id}).data
        return conversations
