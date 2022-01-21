from django.contrib import admin
from .models import Course, EnrolledCourse,  Section, Unit, UnitCompleted
from lessons.models import Lesson, LessonItem
from quizzes.models import Quiz

admin.site.site_header = 'Lakaters - Administration'


class inlineSection(admin.StackedInline):
    model = Section
    extra = 0


class inlineUnit(admin.StackedInline):
    model = Unit
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [inlineUnit]
    list_display = [
        'title',
        'language',

    ]
    list_display_links = [
        'title',

    ]
    list_filter = ['language',
                   'is_active', 'is_active']
    search_fields = ['title']


class SectionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    list_filter = ['course']


class inlineLesson(admin.StackedInline):
    model = Lesson
    extra = 0


class UnitAdmin(admin.ModelAdmin):
    inlines = [inlineLesson]
    list_display = [
        'order', 'id',  'title', 'course'
    ]
    list_display_links = ['id',  'title', 'course']
    list_editable = ['order', ]

    list_filter = ['course']


class UnitCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'unit', 'student', 'is_completed',
    ]
    list_display_links = ['unit', 'student', ]

    list_filter = ['unit', 'student', 'is_completed']


class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = [
        'course', 'student', 'is_enrolled',
    ]
    list_display_links = ['course', 'student', ]

    list_filter = ['course', 'student', 'is_enrolled']


admin.site.register(Course, CourseAdmin)
admin.site.register(UnitCompleted, UnitCompletedAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(EnrolledCourse, EnrolledCourseAdmin)
