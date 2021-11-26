from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'languages'


class Course(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='course_photos', blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    language = models.ForeignKey(
        Language,  blank=True, null=True, max_length=250, on_delete=models.CASCADE)
    is_for_nursery = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'courses'


class Section(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(
        upload_to='section_photos', blank=True, null=True)
    course = models.ForeignKey(
        Course, related_name='Sections', blank=True, null=True, max_length=250, on_delete=models.CASCADE)
    has_units = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'sections'


class Unit(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    section = models.ForeignKey(
        Section, related_name='Units', blank=True, null=True, max_length=250, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'units'
