# Generated by Django 3.2.7 on 2022-01-15 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0019_remove_quiz_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text_option_4',
        ),
    ]