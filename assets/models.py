
import os
from django.db import models
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
from boto3 import Session
from django.core.files.base import ContentFile
from contextlib import closing
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.storage import default_storage as storage
# from google.cloud import texttospeech
# from google.cloud import texttospeech_v1
# import json
# import base64

# import tempfile
# from django.core.files import File
# from io import BytesIO


SERVICE_CHOICES = (
    ("AWS", "AWS"),
    ("GCS", "GCS"),
)

TYPE_CHOICES = (
    ("CLOUD", "CLOUD"),
    ("SELF_RECORD", "SELF_RECORD"),
)


class Voice(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=250, blank=True, null=True)
    service = models.CharField(
        max_length=250, choices=SERVICE_CHOICES, blank=True, null=True)
    nickName = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(
        upload_to='Photos', blank=True, null=True)

    def __str__(self):
        displyName = str(self.nickName + "__" + self.service)
        return displyName

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo)
            memfile = BytesIO()
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size, Image.ANTIALIAS)
                img.save(memfile, 'PNG', quality=95)
                storage.save(self.photo.name, memfile)
                memfile.close()
                img.close()


class Audio(models.Model):
    voice = models.ForeignKey(
        Voice, on_delete=models.CASCADE,  blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    # title = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(
        max_length=250, choices=TYPE_CHOICES, default="CLOUD", blank=True, null=True)
    is_re_record = models.BooleanField(default=True)
    audio = models.FileField(
        upload_to='Audios', blank=True, null=True)

    def __str__(self):
        try:
            nickName = self.voice.nickName
            name = self.voice.name
            text = self.text
            text = text[0:50]
            if nickName != ".":
                objName = text + ": " + nickName
            else:
                objName = text + ": " + name
            return objName
        except:
            return self.text

    class Meta:
        ordering = ['text']

    def save(self, *args, **kwargs):
        # print(self.voice.service)
        try:
            audio_Name = self.text[0:30]
            if self.voice.service == "AWS" and self.is_re_record:
                print("AWS")
                self.is_re_record = False
                # self.type = "AWS"
                aws_access_key_id = getattr(settings, "AWS_POLLY_ACCESS", None)
                aws_secret_access_key = getattr(
                    settings, "AWS_POLLY_SECRET", None)

                voiceId = self.voice.name
                text = self.text

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
                        self.audio.save(str(audio_Name)+'.mp3',
                                        ContentFile(data))
                        super(Audio, self).save(*args, **kwargs)

            if self.voice.service == "GCS" and self.is_re_record:
                print("GCS")
                GCS_CREDENTIALS_FILE_PATH = getattr(
                    settings, "GCS_CREDENTIALS_FILE_PATH", None)

                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCS_CREDENTIALS_FILE_PATH
                # # Instantiates a client
                client = texttospeech_v1.TextToSpeechClient()

                # # Set the text input to be synthesized
                synthesis_input = texttospeech_v1.SynthesisInput(
                    text="Hello, World from google!")

                # Build the voice request, select the language code ("en-US") and the ssml
                # voice gender ("neutral")
                voice = texttospeech_v1.VoiceSelectionParams(
                    language_code="en-US", ssml_gender=texttospeech_v1.SsmlVoiceGender.NEUTRAL)

                # Select the type of audio file you want returned
                audio_config = texttospeech_v1.AudioConfig(
                    audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16)

                voice_name = self.voice.name
                language_code = "-".join(voice_name.split("-")[:2])
                text = self.text

                # print("lan", language_code)
                # print("voic", voice_name)
                # print("text", text)

                text_input = texttospeech_v1.SynthesisInput(text=text)
                voice_params = texttospeech_v1.VoiceSelectionParams(
                    language_code=language_code, name=voice_name)
                # Perform the text-to-speech request on the text input with the selected
                # voice parameters and audio file type
                response = client.synthesize_speech(
                    input=text_input, voice=voice_params, audio_config=audio_config)
                # print(type(response.audio_content))
                audio = response.audio_content
                file_name = '{}.wav'.format(audio_Name)
                test = ContentFile(audio)
                # print(test)
                self.audio.save(file_name, test, save=False)
                super(Audio, self).save(*args, **kwargs)

            else:
                print("else, self recorded")
                super(Audio, self).save(*args, **kwargs)

        except:
            print("Error in loading polly")
            super(Audio, self).save(*args, **kwargs)


class Video(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    video = models.FileField(
        upload_to='Videos', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Photo(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(
        upload_to='Photos', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
