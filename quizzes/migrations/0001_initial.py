# Generated by Django 3.2.7 on 2022-06-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('category', models.CharField(blank=True, choices=[('PHOTO_OPTIONS', 'PHOTO_OPTIONS'), ('TEXT_OPTIONS', 'TEXT_OPTIONS'), ('DRAG', 'DRAG'), ('SPEAK', 'SPEAK'), ('WRITE', 'WRITE'), ('MATCH', 'MATCH'), ('DIALOGUE', 'DIALOGUE'), ('FILL_IN_BLANK', 'FILL_IN_BLANK'), ('FILL_IN_BLANK_WITH_PHOTO', 'FILL_IN_BLANK_WITH_PHOTO'), ('FILL_IN_BLANK_WITH_PHOTO_CON', 'FILL_IN_BLANK_WITH_PHOTO_CON'), ('READING_COMPREHENSION', 'READING_COMPREHENSION'), ('LISTENING_COMPREHENSION', 'LISTENING_COMPREHENSION'), ('EMAIL_FIll_IN_BLANK', 'EMAIL_FIll_IN_BLANK'), ('EMAIL_TRANSLATE_WORD', 'EMAIL_TRANSLATE_WORD'), ('EMAIL_TRANSLATE_SENT', 'EMAIL_TRANSLATE_SENT'), ('PASSAGE_FILL_IN_BLANK', 'PASSAGE_FILL_IN_BLANK'), ('PASSAGE_TRANSLATE_WORD', 'PASSAGE_TRANSLATE_WORD'), ('PASSAGE_TRANSLATE_SENT', 'PASSAGE_TRANSLATE_SENT'), ('CONVERSATION_FILL_IN_BLANK', 'CONVERSATION_FILL_IN_BLANK'), ('CONVERSATION_TRANSLATE', 'CONVERSATION_TRANSLATE')], default='FILL_IN_BLANK_WITH_PHOTO_CON', max_length=250, null=True)),
                ('posType', models.CharField(blank=True, choices=[('NotPos', 'NotPos'), ('Noun', 'Noun'), ('Singular', 'Singular'), ('Place', 'Place'), ('ProperNoun', 'ProperNoun'), ('Plural', 'Plural'), ('Uncountable', 'Uncountable'), ('Possessive', 'Possessive'), ('Verb', 'Verb'), ('PresentTense', 'PresentTense'), ('Infinitive', 'Infinitive'), ('Gerund', 'Gerund'), ('PastTense', 'PastTense'), ('PerfectTense', 'PerfectTense'), ('FuturePerfect', 'FuturePerfect'), ('Participle', 'Participle'), ('PhrasalVerb', 'PhrasalVerb'), ('Adjective', 'Adjective'), ('Negative', 'Negative'), ('Superlative', 'Superlative'), ('Comparative', 'Comparative'), ('Adverb', 'Adverb'), ('Preposition', 'Preposition'), ('QuestionWord', 'QuestionWord'), ('Pronoun', 'Pronoun')], default='NotPos', max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('question', models.TextField(blank=True, max_length=250, null=True)),
                ('answer', models.TextField(blank=True, max_length=250, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('correct_option', models.CharField(blank=True, choices=[('1', 'OPTION_1'), ('2', 'OPTION_2'), ('3', 'OPTION_3'), ('4', 'OPTION_4'), ('ANY', 'ANY')], default='ANY', max_length=250, null=True)),
                ('text_option_1', models.CharField(blank=True, max_length=250, null=True)),
                ('text_option_2', models.CharField(blank=True, max_length=250, null=True)),
                ('text_option_3', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='Photos')),
                ('category', models.CharField(blank=True, choices=[('LISTENING', 'LISTENING'), ('SPEAKING', 'SPEAKING'), ('WRITING', 'WRITING'), ('READING', 'READING'), ('GRAMMAR', 'GRAMMAR'), ('VOCABULARY', 'VOCABULARY'), ('DIALOGUE', 'DIALOGUE'), ('TRANSLATE', 'TRANSLATE'), ('DRAFT EMAIL', 'DRAFT EMAIL'), ('UNIT_TEST', 'UNIT_TEST'), ('REVISION', 'REVISION'), ('MILESTONE', 'MILESTONE'), ('CONVERSATION', 'CONVERSATION'), ('GENERAL_ENGLISH', 'GENERAL_ENGLISH'), ('GENERAL_ARABIC', 'GENERAL_ARABIC'), ('OTHER', 'OTHER')], default='OTHER', max_length=250, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_practice', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'ordering': ['order', 'unit', 'category', 'title'],
            },
        ),
        migrations.CreateModel(
            name='QuizCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('is_completed', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='QuizCompleted', to='quizzes.quiz')),
            ],
        ),
    ]
