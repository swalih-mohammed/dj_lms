from django.db import models
from django.contrib import admin
# from django.forms import TextInput, Textarea
from .models import Quiz, Question, QuizCompleted


class inlineQuestion(admin.StackedInline):
    model = Question
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [inlineQuestion]
    list_display = [
        'order', 'title', 'unit',  'lesson', 'category'
    ]
    list_display_links = ['title', 'lesson', 'unit', 'category']
    list_filter = ['course', 'unit', 'lesson', ]
    list_editable = ['order', ]
    search_fields = ['title']


class QuizCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'student', 'quiz', 'is_completed', 'score'

    ]
    list_filter = ['student', 'quiz', 'is_completed']
    search_fields = ['quiz__title', 'quiz__category']


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'order', 'question', 'category'
    ]
    list_display_links = ['question', ]
    list_filter = ['quiz', 'category']
    list_editable = ['order', ]
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'cols': 40, 'rows': 2, 'size': '100'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    # }


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizCompleted, QuizCompletedAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(PhotoChoices)
# admin.site.register(QuestionType)
