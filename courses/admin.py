from django.contrib import admin
from .models import Language, Course,  Section, Unit
from lessons.models import Lesson, LessonItem
from quizzes.models import Quiz

admin.site.site_header = 'Lakaters - Administration'


class inlineSection(admin.StackedInline):
    model = Section
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [inlineSection]
    list_display = [
        'title',
        'language',

    ]
    list_display_links = [
        'title',

    ]
    list_filter = ['language',
                   'is_for_nursery', 'is_active', 'is_active']
    search_fields = ['title']


class inlineUnit(admin.StackedInline):
    model = Unit
    extra = 0


class SectionAdmin(admin.ModelAdmin):
    inlines = [inlineUnit]
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
        'title',
    ]

    list_filter = ['section']


admin.site.register(Language)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Unit, UnitAdmin)
# admin.site.register(Lesson, LessonAdmin)
