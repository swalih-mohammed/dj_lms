# Generated by Django 3.2.7 on 2022-01-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0023_quizcompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizcompleted',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
