from django.contrib import admin
from .models import Quiz, QuestionType, Question, TextChoices, PhotoChoices, AudioChoices, QuizCompleted


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


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizCompleted, QuizCompletedAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(PhotoChoices)
# admin.site.register(QuestionType)
