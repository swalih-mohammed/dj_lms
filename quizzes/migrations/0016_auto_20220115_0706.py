# Generated by Django 3.2.7 on 2022-01-15 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0015_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='audio_choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='photo_choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text_choices',
        ),
    ]