from django.contrib import admin
from .models import Lesson, LessonItem, LessonCompleted
from quizzes.models import Quiz


class inlineLessonItem(admin.StackedInline):
    model = LessonItem
    extra = 0


class inlineQuiz(admin.StackedInline):
    model = Quiz
    extra = 0


class LessonAdmin(admin.ModelAdmin):
    inlines = [inlineLessonItem, inlineQuiz]
    list_display = [
        'order', 'title', 'unit',
    ]
    list_display_links = ['title', 'unit']
    list_filter = ['unit', ]
    list_editable = ['order', ]


class LessonCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'lesson',  'student', 'is_completed'
    ]
    list_filter = ['lesson', 'student']


class UnitCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'unit',  'student', 'is_completed'
    ]
    list_filter = ['unit', 'student']


admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonItem)
admin.site.register(LessonCompleted, LessonCompletedAdmin)
