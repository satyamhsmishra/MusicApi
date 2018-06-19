from django.contrib import admin
from .models import Album,Song

class AlbumDetails(admin.ModelAdmin):
    list_display = ('artist','album_title','genre','album_logo')

class SongDetails(admin.ModelAdmin):
    list_display = ('song_title','file_type')

admin.site.register(Album,AlbumDetails)
admin.site.register(Song,SongDetails)
