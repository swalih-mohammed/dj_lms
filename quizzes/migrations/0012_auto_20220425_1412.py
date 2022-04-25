# Generated by Django 3.2.7 on 2022-04-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0011_auto_20220419_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiochoices',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='photochoices',
            name='photo',
        ),
        migrations.DeleteModel(
            name='QuestionType',
        ),
        migrations.DeleteModel(
            name='TextChoices',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('PHOTO_OPTIONS', 'PHOTO_OPTIONS'), ('TEXT_OPTIONS', 'TEXT_OPTIONS'), ('DRAG', 'DRAG'), ('SPEAK', 'SPEAK'), ('WRITE', 'WRITE'), ('MATCH', 'MATCH'), ('DIALOGUE', 'DIALOGUE'), ('FILL_IN_BLANK', 'FILL_IN_BLANK'), ('FILL_IN_BLANK_WITH_PHOTO', 'FILL_IN_BLANK_WITH_PHOTO'), ('FILL_IN_BLANK_WITH_PHOTO_CON', 'FILL_IN_BLANK_WITH_PHOTO_CON'), ('READING_COMPREHENSION', 'READING_COMPREHENSION'), ('LISTENING_COMPREHENSION', 'LISTENING_COMPREHENSION'), ('EMAIL_FIll_IN_BLANK', 'EMAIL_FIll_IN_BLANK'), ('EMAIL_TRANSLATE_WORD', 'EMAIL_TRANSLATE_WORD'), ('EMAIL_TRANSLATE_SENT', 'EMAIL_TRANSLATE_SENT'), ('PASSAGE_FILL_IN_BLANK', 'PASSAGE_FILL_IN_BLANK'), ('PASSAGE_TRANSLATE_WORD', 'PASSAGE_TRANSLATE_WORD'), ('PASSAGE_TRANSLATE_SENT', 'PASSAGE_TRANSLATE_SENT')], default='FILL_IN_BLANK_WITH_PHOTO', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.CharField(blank=True, choices=[('LISTENING', 'LISTENING'), ('SPEAKING', 'SPEAKING'), ('WRITING', 'WRITING'), ('READING', 'READING'), ('GRAMMAR', 'GRAMMAR'), ('VOCABULARY', 'VOCABULARY'), ('DIALOGUE', 'DIALOGUE'), ('TRANSLATE', 'TRANSLATE'), ('DRAFT EMAIL', 'DRAFT EMAIL'), ('UNIT_TEST', 'UNIT_TEST'), ('GENERAL_ENGLISH', 'GENERAL_ENGLISH'), ('GENERAL_ARABIC', 'GENERAL_ARABIC'), ('OTHER', 'OTHER')], default='OTHER', max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='AudioChoices',
        ),
        migrations.DeleteModel(
            name='PhotoChoices',
        ),
    ]
