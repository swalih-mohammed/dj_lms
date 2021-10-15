# Generated by Django 3.2.7 on 2021-10-13 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='lesson_photos')),
                ('has_quiz', models.BooleanField(default=False)),
                ('unit', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unitLessons', to='courses.unit')),
            ],
        ),
        migrations.CreateModel(
            name='LessonQuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('has_video', models.BooleanField(default=False)),
                ('video', models.FileField(blank=True, null=True, upload_to='lesson_item_videos')),
                ('has_audio', models.BooleanField(default=False)),
                ('audio', models.FileField(blank=True, null=True, upload_to='lesson_item_audios')),
                ('has_text', models.BooleanField(default=False)),
                ('text', models.CharField(blank=True, max_length=250, null=True)),
                ('has_photo', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='lesson_item_photos')),
                ('lesson', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessonItems', to='lessons.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='LessonCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessonCompleted', to='lessons.lesson')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
