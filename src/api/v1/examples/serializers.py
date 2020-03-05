from src.api.core.serializers import BaseModelSerializer
from src.apps.examples.models import Artist, Album


class AlbumSerializer(BaseModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'album_title', 'artist', 'created', 'modified')


class ArtistSerializer(BaseModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = (
            'id',
            'artist_name',
            'country_code',
            'albums',
            'created',
            'modified',
        )
