from django.db import models

from courses.models import Course, Section, Unit
# from units.models import Unit
from lessons.models import Lesson
from assets.models import Photo, Audio, Video
# from sections.models import Section

QUIZZ_TYPE_CHOICES = (
    ("LESSONBASED", "Lesson_Based"),
    ("UNITBASED", "Unit_Based"),
    ("SECTIONBASED", "Section_Based"),
    ("COURSEBASED", "Course_Based"),
    ("INDIPENDENT", "Independent"),
)
QUESTION_TYPE_CHOICES = (
    ("CHOICE", "Choice"),
    ("DRAG", "DRAG"),
)


class Quiz(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(
        max_length=250, choices=QUIZZ_TYPE_CHOICES, default="Lesson_Based")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courseQuizzes', blank=True, null=True, max_length=250)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name='unitQuizzes', blank=True, null=True, max_length=250)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='unitQuizzes', blank=True, null=True, max_length=250)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lessonQuizzes', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


class TextChoices(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    is_correct_choice = models.BooleanField(default=False)

    def __str__(self):
        if self.is_correct_choice:
            correct = "Y_"
        else:
            correct = "N_"
        return correct+self.title


class PhotoChoices(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ForeignKey(
        Photo, on_delete=models.DO_NOTHING,  blank=True, null=True)
    is_correct_choice = models.BooleanField(default=False)

    def __str__(self):
        if self.is_correct_choice:
            correct = "Y_"
        else:
            correct = "N_"
        return correct+self.title


class AudioChoices(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    is_correct_choice = models.BooleanField(default=False)

    def __str__(self):
        if self.is_correct_choice:
            correct = "Y_"
        else:
            correct = "N_"
        return correct+self.title


class QuestionType(models.Model):
    type = models.CharField(
        max_length=250, choices=QUESTION_TYPE_CHOICES, default="Choice")
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    order = models.SmallIntegerField()
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quizzes', blank=True, null=True, max_length=250)
    questionType = models.ForeignKey(
        QuestionType, on_delete=models.CASCADE, related_name='questions', blank=True, null=True, max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    question = models.CharField(max_length=250, blank=True, null=True)
    answer = models.CharField(max_length=250, blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    photo_choices = models.ManyToManyField(PhotoChoices, blank=True)
    audio_choices = models.ManyToManyField(AudioChoices, blank=True)
    text_choices = models.ManyToManyField(TextChoices, blank=True)

    def __str__(self):
        return self.question
