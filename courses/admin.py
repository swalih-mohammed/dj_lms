from django.contrib import admin
from .models import Course, EnrolledCourse, Unit, UnitCompleted, LiveClass
from lessons.models import Lesson, LessonItem
from quizzes.models import Quiz
from conversations.models import Conversation

admin.site.site_header = 'Lakaters - Administration'


# class inlineSection(admin.StackedInline):
#     model = Section
#     extra = 0


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


# class SectionAdmin(admin.ModelAdmin):
#     list_display = [
#         'title',
#     ]
#     list_filter = ['course']


class inlineLesson(admin.StackedInline):
    model = Lesson
    extra = 0


class inlineQuiz(admin.StackedInline):
    model = Quiz
    extra = 0


class inlineConversation(admin.StackedInline):
    model = Conversation
    extra = 0


class UnitAdmin(admin.ModelAdmin):
    inlines = [inlineLesson, inlineQuiz, inlineConversation]
    list_display = [
        'number', 'order', 'title',
    ]
    list_display_links = ['title', ]
    list_editable = ['order', 'number']

    list_filter = ['course']


class UnitCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'unit', 'student', 'is_completed',
    ]
    list_display_links = ['unit', 'student', ]

    list_filter = ['unit', 'student', 'is_completed']


class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = [
        'course', 'student', 'is_premium',
    ]
    list_display_links = ['course', 'student', ]
    list_filter = ['course', 'student', 'is_enrolled']
    search_fields = ['name']


class LiveClassAdmin(admin.ModelAdmin):
    list_display = [
        'unit', 'title', 'class_date', 'teacher',
    ]
    list_display_links = ['unit', 'title']
    list_filter = ['unit', 'class_date']
    search_fields = ['unit', 'title']


admin.site.register(Course, CourseAdmin)
admin.site.register(LiveClass, LiveClassAdmin)
admin.site.register(UnitCompleted, UnitCompletedAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(EnrolledCourse, EnrolledCourseAdmin)
