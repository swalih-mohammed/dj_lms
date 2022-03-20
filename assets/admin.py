from django.contrib import admin
from .models import Audio, Photo, Video, Voice

# class AudioAdmin(admin.ModelAdmin):


class AudioAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'voice',
    ]
    list_display_links = ['title',  'voice']
    list_filter = ['title', 'voice']
    search_fields = ['title']


admin.site.register(Audio, AudioAdmin)

# admin.site.register(Audio)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Voice)
