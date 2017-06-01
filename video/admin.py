from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_key', 'link']

    def link(self, video):
        return 'https://www.youtube.com/watch?v={}'.format(video.video_key)




admin.site.register(Video, VideoAdmin)
# Register your models here.
