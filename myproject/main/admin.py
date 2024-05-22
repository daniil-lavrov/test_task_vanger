from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import Pictures


class ModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(Pictures, ModelAdmin)