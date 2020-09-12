from django.contrib import admin
from .models import Place, Photo
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class PhotoInline(SortableInlineAdminMixin,admin.TabularInline):
    model = Photo
    fields = ('photo', 'prev_image','photo_order')
    readonly_fields = ["prev_image"]


    def prev_image(self, photo):
        return mark_safe(f'<img src="{photo.photo.url}" height="200">')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
