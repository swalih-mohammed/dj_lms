# Generated by Django 3.2.7 on 2022-01-15 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0016_auto_20220115_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionType',
        ),
    ]
