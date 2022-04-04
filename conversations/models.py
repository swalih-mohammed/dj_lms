from django.db import models
from users.models import User
from courses.models import Unit
from assets.models import Photo, Audio, Video


class Conversation(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE,  related_name='conversations', blank=True, null=True, max_length=250)
    audio_0 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_0', blank=True, null=True)
    audio_1 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_1', blank=True, null=True)
    audio_2 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_2', blank=True, null=True)
    audio_3 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_3', blank=True, null=True)
    audio_4 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_4', blank=True, null=True)
    audio_5 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_5', blank=True, null=True)
    audio_6 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_6', blank=True, null=True)
    audio_7 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_7', blank=True, null=True)
    audio_8 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_8',  blank=True, null=True)
    audio_9 = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING, related_name='audio_9', blank=True, null=True)
    # audio_10 = models.ForeignKey(
    #     Audio, on_delete=models.DO_NOTHING, related_name='audio_10', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'unit', 'title']


class ConversationCompleted(models.Model):

    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation, related_name='ConversationCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.student.username
