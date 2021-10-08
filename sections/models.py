
from django.db import models
from courses.models import Course


class Section(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    course = models.ForeignKey(
        Course, related_name='sections', blank=True, null=True, max_length=250, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'sections'
