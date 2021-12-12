
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from boto3 import Session
from django.core.files.base import ContentFile
from contextlib import closing
from django.conf import settings


class PollySpeaker(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=250, blank=True, null=True)
    nickName = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        displyName = str(self.language + "_" + self.name +
                         "_" + self.gender + "_" + self.nickName)
        return displyName


class Audio(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    is_polly = models.BooleanField(default=False)
    is_re_record = models.BooleanField(default=False)
    pollyText = models.TextField(max_length=250, blank=True, null=True)
    speaker = models.ForeignKey(
        PollySpeaker, on_delete=models.CASCADE, blank=True, null=True)
    audio = models.FileField(
        upload_to='Audios', blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            if self.is_polly and self.is_re_record:
                print("starting to polly")
                self.is_re_record = False
                aws_access_key_id = getattr(settings, "AWS_POLLY_ACCESS", None)
                aws_secret_access_key = getattr(
                    settings, "AWS_POLLY_SECRET", None)

                voiceId = self.speaker.name
                text = self.pollyText

                polly_client = Session(
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name='eu-west-2').client('polly')

                response = polly_client.synthesize_speech(
                    Text=text,
                    OutputFormat="mp3",
                    VoiceId=voiceId)

                if "AudioStream" in response:
                    with closing(response["AudioStream"]) as streamingbody:
                        data = streamingbody.read()
                        self.audio.save(str(self.title)+'.mp3',
                                        ContentFile(data))
                        super(Audio, self).save(*args, **kwargs)

        except:
            print("Error in loading polly")
            super(Audio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    video = models.FileField(
        upload_to='Videos', blank=True, null=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(
        upload_to='Photos', blank=True, null=True)

    def __str__(self):
        return self.title
