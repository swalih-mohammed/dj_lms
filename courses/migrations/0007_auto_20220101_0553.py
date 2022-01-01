# Generated by Django 3.2.7 on 2022-01-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20211231_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_for_nursery',
        ),
        migrations.AddField(
            model_name='course',
            name='order',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('GNERAL_ENGLISH', 'General_English'), ('NURSARY', 'Nursary'), ('SCHOOL_ENGLISH_KERALA', 'School_English_Kerala'), ('GENERAL_ARABIC', 'General_Arabic')], default='General_English', max_length=250),
        ),
    ]
