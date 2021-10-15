from django.contrib import admin
from .models import Quiz, Question, TextChoices, PhotoChoices


class inlineQuestion(admin.StackedInline):
    model = Question
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [inlineQuestion]
    list_display = [
        'title',


    ]
    list_filter = ['lesson']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(TextChoices)
admin.site.register(PhotoChoices)
