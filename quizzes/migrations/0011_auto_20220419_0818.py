# Generated by Django 3.2.7 on 2022-04-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0010_alter_quizcompleted_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizcompleted',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='quizcompleted',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
