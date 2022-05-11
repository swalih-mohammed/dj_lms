from django.db import models
from users.models import User

from PIL import Image
from io import BytesIO
from django.core.files.storage import default_storage as storage


class Language(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'languages'


CATEGORY_CHOICES = (
    ("GENERAL_ENGLISH", "GENERAL_ENGLISH"),
    ("NURSARY", "NURSARY"),
    ("SCHOOL_ENGLISH_KERALA", "SCHOOL_ENGLISH_KERALA"),
    ("GENERAL_ARABIC", "GENERAL_ARABIC"),
)

LANGUAGE_CHOICES = (
    ("ENGLISH", "ENGLISH"),
    ("ARABIC", "ARABIC"),
    ("MALAYALAM", "MALAYALAM"),
    ("SPANISH", "SPANISH"),
    ("FRENCH", "FRENCH"),
    ("GERMAN", "GERMAN"),
)


class Course(models.Model):
    order = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='course_photos', blank=True, null=True)
    certificate = models.ImageField(
        upload_to='course_certificats', blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    category = models.CharField(
        max_length=250, choices=CATEGORY_CHOICES, default="GENERAL_ENGLISH")
    language = models.CharField(
        max_length=250, choices=LANGUAGE_CHOICES, default="ENGLISH")
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
# testing

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'courses'
        ordering = ['order']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo)
            memfile = BytesIO()
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size, Image.ANTIALIAS)
                img.save(memfile, 'PNG', quality=95)
                storage.save(self.photo.name, memfile)
                memfile.close()
                img.close()


class EnrolledCourse(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, related_name='enrolledCourses', on_delete=models.SET_NULL, blank=True, null=True)
    is_enrolled = models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

    class Meta:
        verbose_name_plural = 'Enrollled Courses'
        ordering = ['student', 'course']


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

    def language(self):
        t = self.course.title
        return t

    class Meta:
        verbose_name_plural = 'sections'
        ordering = ['order']


class Unit(models.Model):
    order = models.FloatField(default=0, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    vocab_count = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(
        upload_to='unit_photos', blank=True, null=True)
    course = models.ForeignKey(
        Course, related_name='Units', blank=True, null=True, max_length=250, on_delete=models.CASCADE)
    section = models.ForeignKey(
        Section, related_name='UnitsSections', blank=True, null=True, max_length=250, on_delete=models.CASCADE)

    def __str__(self):
        order = self.order
        course = self.course.title
        unit = course + "_Unit_" + str(order)
        return unit

    class Meta:
        verbose_name_plural = 'units'
        ordering = ['course', 'order']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo)
            memfile = BytesIO()
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size, Image.ANTIALIAS)
                img.save(memfile, 'PNG', quality=95)
                storage.save(self.photo.name, memfile)
                memfile.close()
                img.close()


class UnitCompleted(models.Model):
    student = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, related_name='unitCompleted', on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

    class Meta:
        verbose_name_plural = 'Completedunits'
        ordering = ['student', 'unit']
