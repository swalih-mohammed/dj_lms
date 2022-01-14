from django.db import models

from courses.models import Course, Section, Unit
# from units.models import Unit
from lessons.models import Lesson
from assets.models import Photo, Audio, Video
# from nltk.tokenize import TreebankWordTokenizer

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
    ("DRAG", "Drag"),
    ("MATCH", "Match"),
    ("FILL_IN_BLANK", "Fill_In_Blank"),
    ("SPEAKING", "Speaking"),
    ("WRITING", "Writing"),
)

CORRECT_OPTION_CHOICES = (
    ("OPTION_1", "1"),
    ("OPTION_2", "2"),
    ("OPTION_3", "3"),
    ("OPTION_4", "4"),
)

QUIZZ_CATEGORY_CHOICES = (
    ("LISTENING", "LISTENING"),
    ("SPEAKING", "SPEAKING"),
    ("WRITING", "WRITING"),
    ("READING", "READING"),
    ("GRAMMAR", "GRAMMAR"),
    ("VOCABULARY", "VOCABULARY"),
    ("UNIT_TEST", "UNIT_TEST"),
    ("OTHER", "OTHER"),
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
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    category = models.CharField(
        max_length=250, blank=True, null=True, choices=QUIZZ_CATEGORY_CHOICES, default="OTHER")
    type = models.CharField(
        max_length=250, blank=True, null=True, choices=QUIZZ_TYPE_CHOICES, default="Lesson_Based")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courseQuizzes', blank=True, null=True, max_length=250)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='unitQuizzes', blank=True, null=True, max_length=250)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE,  related_name='unitQuizzes', blank=True, null=True, max_length=250)
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
    questionType = models.ForeignKey(
        QuestionType, on_delete=models.CASCADE, related_name='questions', blank=True, null=True, max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    question = models.CharField(max_length=250, blank=True, null=True)
    answer = models.CharField(max_length=250, blank=True, null=True)
    audio = models.ForeignKey(
        Audio, on_delete=models.DO_NOTHING,  blank=True, null=True)
    correct_option = models.CharField(
        max_length=250, choices=CORRECT_OPTION_CHOICES, blank=True, null=True)
    text_option_1 = models.CharField(max_length=250, blank=True, null=True)
    text_option_2 = models.CharField(max_length=250, blank=True, null=True)
    text_option_3 = models.CharField(max_length=250, blank=True, null=True)
    text_option_4 = models.CharField(max_length=250, blank=True, null=True)
    photo_choices = models.ManyToManyField(PhotoChoices, blank=True)
    audio_choices = models.ManyToManyField(AudioChoices, blank=True)
    text_choices = models.ManyToManyField(TextChoices, blank=True)

    def __str__(self):
        quiz = self.quiz.title
        order = self.order
        name = quiz + "_" + str(order)
        return name

    class Meta:
        ordering = ['order']
