from django.db import models
from django.contrib.auth.models import AbstractUser
# from courses.models import CourseCategory
# import courses.models.CourseCategory


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_course = models.ForeignKey(
        'courses.CourseCategory', blank=True, null=True, on_delete=models.CASCADE)
    level = models.SmallIntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
