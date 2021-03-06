from .models import Photo
from .models import Place
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    fields = ['photo', 'prev_image', 'photo_order']
    readonly_fields = ["prev_image"]

    def prev_image(self, photo):
        if photo.photo:
            return format_html('<img src="{}"  height="200"/>', photo.photo.url)
        else:
            return 'Картинка ещё не загружена'
    prev_image.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
