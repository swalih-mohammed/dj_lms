# Generated by Django 3.2.7 on 2021-12-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_alter_lessonitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonitem',
            name='content',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]