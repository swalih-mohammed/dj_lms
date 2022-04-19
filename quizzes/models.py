from django.db import models
from users.models import User
from courses.models import Course, Section, Unit
# from units.models import Unit
from lessons.models import Lesson
from assets.models import Photo, Audio, Video
from PIL import Image
from io import BytesIO
from django.core.files.storage import default_storage as storage

# from nltk.tokenize import TreebankWordTokenizer

# from sections.models import Section


QUESTION_TYPE_CHOICES = (
    ("CHOICE", "Choice"),
    ("DRAG", "Drag"),
    ("MATCH", "Match"),
    ("FILL_IN_BLANK", "Fill_In_Blank"),
    ("SPEAKING", "Speaking"),
    ("WRITING", "Writing"),
    ("READING_COMPREHENSION", "READING_COMPREHENSION"),
    ("LISTENING_COMPREHENSION", "LISTENING_COMPREHENSION"),
)

CORRECT_OPTION_CHOICES = (
    ("1", "OPTION_1"),
    ("2", "OPTION_2"),
    ("3", "OPTION_3"),
    ("4", "OPTION_4"),
    ("ANY", "ANY"),

)

QUIZZ_CATEGORY_CHOICES = (
    ("LISTENING", "LISTENING"),
    ("SPEAKING", "SPEAKING"),
    ("WRITING", "WRITING"),
    ("READING", "READING"),
    ("GRAMMAR", "GRAMMAR"),
    ("VOCABULARY", "VOCABULARY"),
    ("DIALOGUE", "DIALOGUE"),
    ("TRANSLATE", "TRANSLATE"),
    ("UNIT_TEST", "UNIT_TEST"),
    ("GENERAL_ENGLISH", "GENERAL_ENGLISH"),
    ("GENERAL_ARABIC", "GENERAL_ARABIC"),
    ("OTHER", "OTHER"),
)


QUESTION_CATEGORY_CHOICES = (
    ("PHOTO_OPTIONS", "PHOTO_OPTIONS"),
    ("TEXT_OPTIONS", "TEXT_OPTIONS"),
    ("DRAG", "DRAG"),
    ("SPEAK", "SPEAK"),
    ("WRITE", "WRITE"),
    ("MATCH", "MATCH"),
    ("DIALOGUE", "DIALOGUE"),
    ("FILL_IN_BLANK", "FILL_IN_BLANK"),
    ("FILL_IN_BLANK_WITH_PHOTO", "FILL_IN_BLANK_WITH_PHOTO"),
    ("FILL_IN_BLANK_WITH_PHOTO_CON", "FILL_IN_BLANK_WITH_PHOTO_CON"),
    ("READING_COMPREHENSION", "READING_COMPREHENSION"),
    ("LISTENING_COMPREHENSION", "LISTENING_COMPREHENSION"),
)

QUESTION_ASSET_TYPE_CHOICES = (
    ("PHOTO", "Photo"),
    ("TEXT", "Text"),
    ("AUDIO", "Audio"),
    ("VIDEO", "Video"),
    ("OTHER", "Other"),
)

POS_CHOICES = (
    ("NotPos", "NotPos"),
    ("Noun", "Noun"),
    ("Singular", "Singular"),
    ("Place", "Place"),
    ("ProperNoun", "ProperNoun"),
    ("Plural", "Plural"),
    ("Uncountable", "Uncountable"),
    ("Possessive", "Possessive"),
    ("Verb", "Verb"),
    ("PresentTense", "PresentTense"),
    ("Infinitive", "Infinitive"),
    ("Gerund", "Gerund"),
    ("PastTense", "PastTense"),
    ("PerfectTense", "PerfectTense"),
    ("FuturePerfect", "FuturePerfect"),
    ("Participle", "Participle"),
    ("PhrasalVerb", "PhrasalVerb"),
    ("Adjective", "Adjective"),
    ("Negative", "Negative"),
    ("Superlative", "Superlative"),
    ("Comparative", "Comparative"),
    ("Adverb", "Adverb"),
    ("Preposition", "Preposition"),
    ("QuestionWord", "QuestionWord"),
    ("Pronoun", "Pronoun"),

)


class Quiz(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(
        upload_to='Photos', blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    category = models.CharField(
        max_length=250, blank=True, null=True, choices=QUIZZ_CATEGORY_CHOICES, default="OTHER")
    text = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE,  related_name='unitQuizzes', blank=True, null=True, max_length=250)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lessonQuizzes', blank=True, null=True, max_length=250)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courseQuizzes', blank=True, null=True, max_length=250)

    def __str__(self):
        try:
            category = self.category
            unit = self.unit.title
            title = self.title
            name = category + "_" + unit + "_" + title
            return name
        except:
            return self.title

    class Meta:
        ordering = ['order', 'unit', 'category', 'title']

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
    assetType = models.CharField(
        max_length=250, choices=QUESTION_ASSET_TYPE_CHOICES, default="Other")
    title = models.CharField(max_length=250, blank=True, null=True)
    has_audio = models.BooleanField(default=False)
    pos = models.CharField(
        max_length=250, choices=POS_CHOICES, default="NotPos")

    def __str__(self):
        Type = self.type
        Asset = self.assetType
        if self.has_audio:
            Audio = "HasAudio"
        else:
            Audio = "NoAudio"
        return Type+"_"+Asset + "_"+Audio+"_"+self.title

    class Meta:
        ordering = ['type', 'assetType', 'has_audio', 'pos']


class Question(models.Model):
    order = models.SmallIntegerField()
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quizzes', blank=True, null=True, max_length=250)
    category = models.CharField(
        max_length=250, choices=QUESTION_CATEGORY_CHOICES, default="FILL_IN_BLANK_WITH_PHOTO", blank=True, null=True)
    posType = models.CharField(
        max_length=250, choices=POS_CHOICES, blank=True, null=True, default="NotPos")
    title = models.CharField(max_length=250, blank=True, null=True)
    question = models.TextField(max_length=250, blank=True, null=True)
    answer = models.TextField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    correct_option = models.CharField(
        max_length=250, choices=CORRECT_OPTION_CHOICES, default="ANY", blank=True, null=True)

    text_option_1 = models.CharField(max_length=250, blank=True, null=True)
    text_option_2 = models.CharField(max_length=250, blank=True, null=True)
    text_option_3 = models.CharField(max_length=250, blank=True, null=True)

    photo_option_1 = models.ForeignKey(
        Photo, related_name='photo_1', on_delete=models.DO_NOTHING,  blank=True, null=True)
    photo_option_2 = models.ForeignKey(
        Photo,  related_name='photo_2', on_delete=models.DO_NOTHING,  blank=True, null=True)
    photo_option_3 = models.ForeignKey(
        Photo,  related_name='photo_3', on_delete=models.DO_NOTHING,  blank=True, null=True)
    photo_option_4 = models.ForeignKey(
        Photo,  related_name='photo_4', on_delete=models.DO_NOTHING,  blank=True, null=True)

    def __str__(self):
        quiz = self.quiz.title
        order = self.order
        name = quiz + "_" + str(order)
        return name

    class Meta:
        ordering = ['order']

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


class QuizCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, related_name='QuizCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, default=0)
    is_completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.quiz.title + "_" + self.student.username
