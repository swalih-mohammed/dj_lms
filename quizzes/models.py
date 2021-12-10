from django.db import models

from courses.models import Course, Section, Unit
# from units.models import Unit
from lessons.models import Lesson
# from sections.models import Section

# chagne


class Quiz(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)

    is_indipendent = models.BooleanField(default=False)
    is_course_based = models.BooleanField(default=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courseQuizzes', blank=True, null=True, max_length=250)
    is_section_based = models.BooleanField(default=False)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='unitQuizzes', blank=True, null=True, max_length=250)
    is_unit_based = models.BooleanField(default=False)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='unitQuizzes', blank=True, null=True, max_length=250)
    is_lesson_based = models.BooleanField(default=False)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lessonQuizzes', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


class TextChoices(models.Model):
    is_correct_choice = models.BooleanField(default=False)
    title = models.CharField(max_length=250, blank=True, null=True)


class PhotoChoices(models.Model):
    is_correct_choice = models.BooleanField(default=False)
    photo = models.ImageField(
        upload_to='quiz_photo_choices', blank=True, null=True)


class QuestionType(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questionQuizzes', blank=True, null=True, max_length=250)
    order = models.SmallIntegerField()
    question = models.CharField(max_length=250, blank=True, null=True)
    has_photo_choices = models.BooleanField(default=False)
    photo_choices = models.ManyToManyField(PhotoChoices, blank=True)
    has_text_choices = models.BooleanField(default=False)
    text_choices = models.ManyToManyField(TextChoices, blank=True)
    has_video = models.BooleanField(default=False)
    video = models.FileField(
        upload_to='quiz_videos', blank=True, null=True)
    has_audio = models.BooleanField(default=False)
    audio = models.FileField(
        upload_to='quiz_audios', blank=True, null=True)
    has_text = models.BooleanField(default=False)
    text = models.CharField(max_length=250, blank=True, null=True)
    has_photo = models.BooleanField(default=False)
    photo = models.ImageField(
        upload_to='quiz_photos', blank=True, null=True)
    questionType = models.ForeignKey(
        QuestionType, on_delete=models.CASCADE, related_name='questions', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.question
