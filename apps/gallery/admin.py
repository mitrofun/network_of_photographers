from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'name', 'content_type', 'object_id', 'is_approved')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200" />')
        return ''

    image_preview.short_description = 'Preview'
