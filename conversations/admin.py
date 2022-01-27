from django.contrib import admin
from .models import Conversation

# Register your models here.


class CoversationAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'unit'
    ]
    list_display_links = ['title', ]
    list_filter = ['unit']
    # list_editable = ['title', ]


admin.site.register(Conversation, CoversationAdmin)
