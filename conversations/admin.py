from django.contrib import admin
from .models import Conversation, ConversationCompleted

# Register your models here.


class CoversationAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'unit'
    ]
    list_display_links = ['title', ]
    list_filter = ['unit']
    # list_editable = ['title', ]


class ConversationCompletedAdmin(admin.ModelAdmin):
    list_display = [
        'student', 'conversation', 'is_completed'
    ]
    list_display_links = ['student', 'conversation']
    list_filter = ['conversation', 'student']
    list_editable = ['is_completed', ]


admin.site.register(Conversation, CoversationAdmin)
admin.site.register(ConversationCompleted, ConversationCompletedAdmin)
