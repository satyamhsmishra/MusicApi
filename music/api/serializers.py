from music.models import Album,Song
from rest_framework import serializers

class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields='__all__'