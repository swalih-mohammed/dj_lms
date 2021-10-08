
from django.db import models
from sections.models import Section


class SectionTest(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    section = models.ForeignKey(
        Section, blank=True, null=True, max_length=250, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'sectionTests'
