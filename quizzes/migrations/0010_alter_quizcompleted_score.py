# Generated by Django 3.2.7 on 2022-04-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0009_auto_20220418_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizcompleted',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
