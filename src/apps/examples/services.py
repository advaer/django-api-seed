from src.apps.core.services import BaseService, GenericBaseService

from .models import Artist, Album


class ArtistService(GenericBaseService):
    """
    Generic Service for Farm model CRUD
    """
    model_class = Artist


class AlbumService(GenericBaseService):
    """
    Generic Service for Field model CRUD
    """
    model_class = Album


class ArtistAlbumService(BaseService):
    """
    Custom Service to manage Farm Field relations
    """
    @classmethod
    def get_artist_albums(cls, pk):
        artist = Artist.objects.get_object(pk)
        artist.fields = artist.album_set.all()
        return artist

    @classmethod
    def get_artist_albums_list(cls):
        artists = ArtistService.get_list()
        for artist in artists:
            artist.albums = artist.field_set.all()
        return artists
