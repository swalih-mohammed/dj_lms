# Generated by Django 3.2.7 on 2022-01-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoncompleted',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
