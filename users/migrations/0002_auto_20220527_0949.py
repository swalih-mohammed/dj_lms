# Generated by Django 3.2.7 on 2022-05-27 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20220527_0941'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.coursecategory'),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]