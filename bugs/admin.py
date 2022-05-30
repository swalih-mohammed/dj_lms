from django.contrib import admin
from .models import Bug

# Register your models here.


class BugAdmin(admin.ModelAdmin):
    list_display = [
        'message',
    ]
    list_display_links = ['message']
    list_filter = ['created_at', 'updated_at',
                   'is_resolved', 'course', 'user', ]
    search_fields = ['message']


admin.site.register(Bug, BugAdmin)
