from django.contrib import admin
from .models import Audio, Photo, Video, Voice

# class AudioAdmin(admin.ModelAdmin):


class AudioAdmin(admin.ModelAdmin):
    list_display = [
        'text',
    ]
    list_display_links = ['text']
    list_filter = ['voice__service']
    search_fields = ['text']


admin.site.register(Audio, AudioAdmin)

# admin.site.register(Audio)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Voice)
