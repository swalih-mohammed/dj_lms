from django.contrib import admin
from .models import UnitTest, Question, Choice

admin.site.register(UnitTest)
admin.site.register(Question)
admin.site.register(Choice)
