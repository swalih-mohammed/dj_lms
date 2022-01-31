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

    def create(self, request):
        data = request.data
        print("data in conv create", data)
        conversation = Conversation.objects.get(id=data['conversationId'])
        student = User.objects.get(username=data['username'])
        # conversation = Conversation.objects.get(id=1)
        # student = User.objects.get(username='sibiyan')
        unit = Unit.objects.get(pk=conversation.unit.id)

        unitCompleted_qs = UnitCompleted.objects.filter(
            student=student, is_completed=True, unit=unit)
        if not len(unitCompleted_qs) > 0:

            # lessons progress
            lessons_in_unit = Lesson.objects.filter(unit=unit)
            completed_lessons = LessonCompleted.objects.filter(
                student=student, is_completed=True, lesson__unit=unit)

            # quiz progress
            quizzes_in_unit = Quiz.objects.filter(unit=unit)
            completed_quizzes = QuizCompleted.objects.filter(
                student=student, is_completed=True, quiz__unit=unit).distinct()

            # conversation progress
            conversation_in_unit = Conversation.objects.filter(unit=unit)
            completed_conversations = ConversationCompleted.objects.filter(
                student=student, is_completed=True, conversation__unit=unit).distinct()

            total_items = len(lessons_in_unit) + \
                len(quizzes_in_unit) + len(conversation_in_unit)
            total_completed_items = len(
                completed_lessons) + len(completed_quizzes) + len(completed_conversations)+1

            if total_completed_items >= total_items:
                print("all completed from quiz complete create")
                unitCompleted = UnitCompleted.objects.create(
                    student=student,
                    unit=unit,
                    is_completed=True
                )
                unitCompleted.save()
        conversationCompleted_qs = ConversationCompleted.objects.filter(
            student=student, is_completed=True, conversation=conversation)
        if not len(conversationCompleted_qs) > 0:
            conversationCompleted = ConversationCompleted()
            conversationCompleted.conversation = conversation
            conversationCompleted.student = student
            conversationCompleted.is_completed = True
            conversationCompleted.save()
            return conversationCompleted
        return
        print("conversation already completed")


class ConversationSerializer(serializers.ModelSerializer):
    conversationCompleted = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        # fields = ('__all__')
        fields = ['id', 'title', 'order', 'subtitle',
                  'unit', 'conversationCompleted']

    def get_conversationCompleted(self, obj):
        try:
            username = self.context['username']
            user = User.objects.get(username=username)
            userId = user.id
            conversationCompleted = ConversationCompletedSerializer(
                obj.ConversationCompleted.filter(student=userId), many=True).data
            # print(len(quizCompleted))
            if conversationCompleted:
                if len(conversationCompleted) > 0:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False


class ConversationDetailSerializer(serializers.ModelSerializer):
    audio_0 = AudioSerializer(read_only=True)
    audio_1 = AudioSerializer(read_only=True)
    audio_2 = AudioSerializer(read_only=True)
    audio_3 = AudioSerializer(read_only=True)
    audio_4 = AudioSerializer(read_only=True)
    audio_5 = AudioSerializer(read_only=True)
    audio_6 = AudioSerializer(read_only=True)
    audio_7 = AudioSerializer(read_only=True)
    audio_8 = AudioSerializer(read_only=True)
    audio_9 = AudioSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = ('__all__')
