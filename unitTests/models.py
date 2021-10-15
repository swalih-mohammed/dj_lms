
# from users.models import User
# from django.contrib.auth.models import User
from django.db import models
from units.models import Unit
from users.models import User


class UnitTest(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    unit = models.ForeignKey(
        Unit, related_name='unitTests', blank=True,  null=True, max_length=250, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name_plural = 'unitTests'


class GradedUnitTest(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()
    is_completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.student.username


class Choice(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    unit = models.ForeignKey(
        UnitTest, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question


# class PhotoQuiz(models.Model):
#     title = models.CharField(max_length=250, blank=True, null=True)
#     unit = models.ForeignKey(
#         UnitTest, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
#     order = models.SmallIntegerField()

#     def __str__(self):
#         return self.question
