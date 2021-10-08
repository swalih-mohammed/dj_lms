from django.contrib import admin
from .models import Lesson, LessonQuestion, LessonQuestionChoice

admin.site.register(Lesson)
admin.site.register(LessonQuestion)
admin.site.register(LessonQuestionChoice)
