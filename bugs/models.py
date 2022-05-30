from django.db import models
from courses.models import Course, Unit
from quizzes.models import Quiz
from conversations.models import Conversation
from users.models import User


# Create your models here.

class Bug(models.Model):
    message = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name='course_bugs', blank=True, null=True, )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,  related_name='course_bugs', blank=True, null=True, )
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE,  related_name='unit_buts', blank=True, null=True,)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE,  related_name='quiz_bugs', blank=True, null=True, )
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE,  related_name='conversation_bugs', blank=True, null=True, )
