# Generated by Django 3.2.7 on 2022-01-27 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0025_conversation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]