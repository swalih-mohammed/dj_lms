from django.contrib import admin
from .models import Lesson, LessonItem
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
    list_filter = ['unit', ]


admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonItem)
