from django.contrib import admin
from .models import Audio, Photo, Video, Voice

# class AudioAdmin(admin.ModelAdmin):


admin.site.register(Audio)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Voice)
