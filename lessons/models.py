
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from courses.models import Unit, UnitCompleted
from assets.models import Audio, Video, Photo

LESSON_ITEM_TYPE_CHOICES = (
    ("ONLY_VIDEO", "Only_Video"),
    ("ONLY_PHOTO", "Only_Photo"),
    ("PHOTO_AND_AUDIO", "Photo_And_Audio"),
)


class Lesson(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='lesson_photos', blank=True, null=True)
    video = models.ForeignKey(
        Video, on_delete=models.DO_NOTHING,  blank=True, null=True)
    unit = models.ForeignKey(Unit, related_name='Lessons',
                             on_delete=models.CASCADE,  blank=True, null=True, max_length=250)
    has_quiz = models.BooleanField(default=False)

    def __str__(self):
        unit = self.unit.title
        return self.title + "_" + unit

    class Meta:
        ordering = ['unit', 'order']


class LessonItem(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson, related_name='LessonItems', on_delete=models.CASCADE, blank=True, null=True, max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(max_length=250, blank=True, null=True)
    type = models.CharField(
        max_length=250, choices=LESSON_ITEM_TYPE_CHOICES, default="PHOTO_AND_AUDIO")

    photo = models.ForeignKey(
        Photo, on_delete=models.DO_NOTHING,  blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    video = models.ForeignKey(
        Video, on_delete=models.DO_NOTHING,  blank=True, null=True)

    def __str__(self):
        return self.title

    def photo_url(self):
        if self.photo:
            return self.photo.url

    class Meta:
        ordering = ['order']


class LessonCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name='lessonCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.student.username
