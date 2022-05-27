# Generated by Django 3.2.7 on 2022-05-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_teacher'),
        ('courses', '0015_remove_liveclass_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclass',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]
