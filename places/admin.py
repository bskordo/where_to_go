from django.contrib import admin
from .models import Place, Photo
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    fields = ['photo', 'prev_image', 'photo_order']
    readonly_fields = ["prev_image"]

    def prev_image(self, photo):
        try:
            return format_html('<img src="{}"  height="200"/>'.format(photo.photo.url))
        except:
            return format_html('Картинка ещё не загружена')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
