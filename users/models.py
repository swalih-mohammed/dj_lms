from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
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


@receiver(post_save, sender=User)
def create_or_update_user_student(sender, instance, created, **kwargs):
    try:
        from courses.models import CourseCategory
        current_course = CourseCategory.objects.filter(order=1).last()
        if current_course:
            if created:
                Student.objects.create(
                    user=instance, current_course=current_course)
        else:
            if created:
                Student.objects.create(user=instance)
        instance.student.save()
    except:
        print("error in except creating student")
        instance.student.save()
