# Generated by Django 3.2.7 on 2022-01-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0020_remove_question_text_option_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='order',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]