# Generated by Django 3.2.7 on 2022-04-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_auto_20220404_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('PHOTO_OPTIONS', 'PHOTO_OPTIONS'), ('TEXT_OPTIONS', 'TEXT_OPTIONS'), ('DRAG', 'DRAG'), ('SPEAK', 'SPEAK'), ('WRITE', 'WRITE'), ('MATCH', 'MATCH'), ('FILL_IN_BLANK', 'FILL_IN_BLANK'), ('FILL_IN_BLANK_WITH_PHOTO', 'FILL_IN_BLANK_WITH_PHOTO'), ('FILL_IN_BLANK_WITH_PHOTO_CON', 'FILL_IN_BLANK_WITH_PHOTO_CON')], max_length=250, null=True),
        ),
    ]