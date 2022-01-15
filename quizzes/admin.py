from django.contrib import admin
from .models import Quiz, QuestionType, Question, TextChoices, PhotoChoices, AudioChoices


class inlineQuestion(admin.StackedInline):
    model = Question
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [inlineQuestion]
    list_display = [
        'title', 'lesson', 'unit', 'category'


    ]
    list_filter = ['unit', 'lesson']


admin.site.register(Quiz, QuizAdmin)
# admin.site.register(TextChoices)
# admin.site.register(AudioChoices)
# admin.site.register(PhotoChoices)
# admin.site.register(QuestionType)
