# Generated by Django 3.2.7 on 2022-06-25 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitcompleted',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unitcompleted',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unitCompleted', to='courses.unit'),
        ),
        migrations.AddField(
            model_name='unit',
            name='course',
            field=models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Units', to='courses.course'),
        ),
        migrations.AddField(
            model_name='liveclass',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
        migrations.AddField(
            model_name='liveclass',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='courses.unit'),
        ),
        migrations.AddField(
            model_name='enrolledcourse',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrolledCourses', to='courses.course'),
        ),
        migrations.AddField(
            model_name='enrolledcourse',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courseCategories', to='courses.coursecategory'),
        ),
    ]
