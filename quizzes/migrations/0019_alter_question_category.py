# Generated by Django 3.2.7 on 2022-05-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0018_auto_20220511_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('PHOTO_OPTIONS', 'PHOTO_OPTIONS'), ('TEXT_OPTIONS', 'TEXT_OPTIONS'), ('DRAG', 'DRAG'), ('SPEAK', 'SPEAK'), ('WRITE', 'WRITE'), ('MATCH', 'MATCH'), ('DIALOGUE', 'DIALOGUE'), ('FILL_IN_BLANK', 'FILL_IN_BLANK'), ('FILL_IN_BLANK_WITH_PHOTO', 'FILL_IN_BLANK_WITH_PHOTO'), ('FILL_IN_BLANK_WITH_PHOTO_CON', 'FILL_IN_BLANK_WITH_PHOTO_CON'), ('READING_COMPREHENSION', 'READING_COMPREHENSION'), ('LISTENING_COMPREHENSION', 'LISTENING_COMPREHENSION'), ('EMAIL_FIll_IN_BLANK', 'EMAIL_FIll_IN_BLANK'), ('EMAIL_TRANSLATE_WORD', 'EMAIL_TRANSLATE_WORD'), ('EMAIL_TRANSLATE_SENT', 'EMAIL_TRANSLATE_SENT'), ('PASSAGE_FILL_IN_BLANK', 'PASSAGE_FILL_IN_BLANK'), ('PASSAGE_TRANSLATE_WORD', 'PASSAGE_TRANSLATE_WORD'), ('PASSAGE_TRANSLATE_SENT', 'PASSAGE_TRANSLATE_SENT'), ('CONVERSATION_FILL_IN_BLANK', 'CONVERSATION_FILL_IN_BLANK'), ('CONVERSATION_TRANSLATE', 'CONVERSATION_TRANSLATE')], default='FILL_IN_BLANK_WITH_PHOTO_CON', max_length=250, null=True),
        ),
    ]
