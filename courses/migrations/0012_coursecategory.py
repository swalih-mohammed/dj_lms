# Generated by Django 3.2.7 on 2022-05-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20220527_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('GENERAL_ENGLISH', 'GENERAL_ENGLISH'), ('NURSARY', 'NURSARY'), ('SCHOOL_ENGLISH_KERALA', 'SCHOOL_ENGLISH_KERALA'), ('GENERAL_ARABIC', 'GENERAL_ARABIC')], max_length=250, null=True)),
                ('order', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]