
from django.db import models
from users.models import User
from courses.models import Unit, Section


class Lesson(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='lesson_photos', blank=True, null=True)
    has_quiz = models.BooleanField(default=False)
    section = models.ForeignKey(
        Section, related_name='Sections', blank=True, null=True, max_length=250, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='Lessons',
                             on_delete=models.CASCADE,  blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


class LessonItem(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    has_video = models.BooleanField(default=False)
    video = models.FileField(
        upload_to='lesson_item_videos', blank=True, null=True)
    has_audio = models.BooleanField(default=False)
    audio = models.FileField(
        upload_to='lesson_item_audios', blank=True, null=True)
    has_text = models.BooleanField(default=False)
    text = models.CharField(max_length=250, blank=True, null=True)
    has_photo = models.BooleanField(default=False)
    photo = models.ImageField(
        upload_to='lesson_item_photos', blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson, related_name='LessonItems', on_delete=models.CASCADE, blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


class LessonQuestionChoice(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class LessonCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name='lessonCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.student.username
