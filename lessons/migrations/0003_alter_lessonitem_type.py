# Generated by Django 3.2.7 on 2021-12-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20211211_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonitem',
            name='type',
            field=models.CharField(choices=[('ONLY_VIDEO', 'Only_Video'), ('ONLY_PHOTO', 'Only_Photo'), ('PHOTO_AND_AUDIO', 'Photo_And_Audio')], default='Photo_And_Audio', max_length=250),
        ),
    ]