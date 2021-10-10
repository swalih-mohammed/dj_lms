
from django.db import models
from users.models import User
from units.models import Unit
from sections.models import Section


class Lesson(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    has_video = models.BooleanField(default=False)
    has_audi = models.BooleanField(default=False)
    has_text = models.BooleanField(default=False)
    has_photo = models.BooleanField(default=False)
    readingtText = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='lesson_photos', blank=True, null=True)
    video = models.FileField(upload_to='lesson_video', blank=True, null=True)
    audio = models.FileField(upload_to='lesson_audio', blank=True, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='unitLessons', blank=True, null=True, max_length=250)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='sectionLessons', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


class LessonQuestionChoice(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class LessonQuestion(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    choices = models.ManyToManyField(LessonQuestionChoice)
    answer = models.CharField(max_length=250, blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lessonsQuestions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question


class LessonCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name='lessonCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.student.username
