from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

from .models import Pictures


class ModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_image')

    def get_image(self, obj):
        thumbnail = get_thumbnailer(obj.img).get_thumbnail({
            'size': (100, 100),
            'crop': True,
        })

        thumbnail_url = thumbnail.url
        return mark_safe(f'<img src="{thumbnail_url}" />')

    get_image.short_description = "Изображение"


admin.site.register(Pictures, ModelAdmin)