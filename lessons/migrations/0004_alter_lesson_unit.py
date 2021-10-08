# Generated by Django 3.2.7 on 2021-09-30 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_alter_unit_section'),
        ('lessons', '0003_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unitLessons', to='units.unit'),
        ),
    ]
