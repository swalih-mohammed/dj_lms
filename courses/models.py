from django.db import models
from users.models import User
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    course_fee = models.CharField(
        max_length=10, blank=True, null=True, default="1000")
    discount = models.CharField(
        max_length=10, blank=True, null=True, default="0.2")
    is_free = models.BooleanField(blank=True, null=True, default=False)
    is_active = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'courses'
        ordering = ['-order']

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
    current_unit = models.IntegerField(default=1, blank=True, null=True)
    is_enrolled = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.student.username + "_" + self.course.title

    class Meta:
        verbose_name_plural = 'Enrollled Courses'
        ordering = ['student', 'course']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(EnrolledCourse, self).save(*args, **kwargs)


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
    number = models.IntegerField(default=1, blank=True, null=True)
    order = models.FloatField(default=1, blank=True, null=True)
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


class LiveClass(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(
        upload_to='photos', blank=True, null=True)
    unit = models.ForeignKey(
        Unit, related_name="units", blank=True, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    class_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.unit) + self.title

    class Meta:
        verbose_name_plural = 'LiveClasses'
        ordering = ['class_date']


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

    # def save(self, *args, **kwargs):
    #     if self.is_completed:
    #         ErnolledCourse = EnrolledCourse.objects.filter(
    #             student=self.student, course=self.unit.course)
    #         ErnolledCourse[0].current_unit = 2
    #         ErnolledCourse[0].save()
    #         print("saved", ErnolledCourse[0])
    #     return super(UnitCompleted, self).save(*args, **kwargs)


# @receiver(post_save, sender=UnitCompleted)
# def update_current_unit(sender, instance, **kwargs):
#     ErnolledCourse = EnrolledCourse.objects.filter(
#         student=instance.student, course=instance.unit.course)
    # print("post save")
    # if instance.is_completed:
    #     ErnolledCourse = EnrolledCourse.objects.filter(
    #         student=instance.student, course=instance.unit.course)
    #     ErnolledCourse[0].is_premium = True
    #     print(ErnolledCourse[0].current_unit)
    #     ErnolledCourse[0].save()
    #     print("saved", ErnolledCourse[0])
