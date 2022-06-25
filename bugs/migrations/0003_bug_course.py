# Generated by Django 3.2.7 on 2022-06-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('bugs', '0002_bug_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_bugs', to='courses.course'),
        ),
    ]
