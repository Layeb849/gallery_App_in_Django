from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "album", "caption", "uploaded_at")
    search_fields = ("caption", "album__name")
    ordering = ("-uploaded_at",)
