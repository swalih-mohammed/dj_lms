# Generated by Django 3.2.7 on 2022-05-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_student_current_course'),
        ('courses', '0020_alter_enrolledcourse_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveclass',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]
