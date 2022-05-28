# Generated by Django 3.2.7 on 2022-05-27 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_student_current_course'),
        ('courses', '0019_auto_20220527_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourse',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]