
from django.db import models
from users.models import User
from courses.models import Unit, Section
from assets.models import Audio, Video, Photo


class Lesson(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='lesson_photos', blank=True, null=True)
    section = models.ForeignKey(
        Section, related_name='Sections', blank=True, null=True, max_length=250, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='Lessons',
                             on_delete=models.CASCADE,  blank=True, null=True, max_length=250)
    has_quiz = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def language(self):
        try:
            t = slef.section.course.language
            return t
        except:
            return


LESSON_ITEM_TYPE_CHOICES = (
    ("ONLY_VIDEO", "Only_Video"),
    ("ONLY_PHOTO", "Only_Photo"),
    ("PHOTO_AND_AUDIO", "Photo_And_Audio"),
)


class LessonItem(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson, related_name='LessonItems', on_delete=models.CASCADE, blank=True, null=True, max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    content = models.TextField(max_length=250, blank=True, null=True)
    type = models.CharField(
        max_length=250, choices=LESSON_ITEM_TYPE_CHOICES, default="Photo_And_Audio")

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


class LessonCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, related_name='lessonCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.student.username
