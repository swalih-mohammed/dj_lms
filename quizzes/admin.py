from django.contrib import admin
from .models import Quiz, QuestionType, Question, TextChoices, PhotoChoices, AudioChoices, QuizCompleted


class inlineQuestion(admin.StackedInline):
    model = Question
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [inlineQuestion]
    list_display = [
        'title', 'lesson', 'unit', 'category'


    ]
    list_filter = ['unit', 'lesson']


class QuizCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'student', 'quiz', 'is_completed'

    ]
    list_filter = ['student', 'quiz', 'is_completed']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizCompleted, QuizCompletedAdmin)
# admin.site.register(AudioChoices)
# admin.site.register(PhotoChoices)
# admin.site.register(QuestionType)
