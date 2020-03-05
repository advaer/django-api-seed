from django.http import Http404
from rest_framework.response import Response

from src.api.core.views import BaseAPIView, GenericAPIListView, GenericAPIView
from src.apps.examples.services import ArtistAlbumService, ArtistService, AlbumService

from .serializers import ArtistSerializer, AlbumSerializer


class ArtistListView(GenericAPIListView):
    serializer_class = ArtistSerializer
    service_class = ArtistService


class ArtistView(GenericAPIView):
    serializer_class = ArtistSerializer
    service_class = ArtistService


class AlbumListView(GenericAPIListView):
    serializer_class = AlbumSerializer
    service_class = AlbumService


class AlbumView(GenericAPIView):
    serializer_class = AlbumSerializer
    service_class = AlbumService


class ArtistAlbumsListView(BaseAPIView):

    def get(self, request, format=None):
        albums = ArtistAlbumService.get_artist_albums_list()
        serializer = ArtistSerializer(albums, many=True)
        return Response(serializer.data)


class ArtistAlbumsView(BaseAPIView):

    def get(self, request, pk, format=None):
        try:
            farm = ArtistAlbumService.get_artist_albums(pk)
        except KeyError:
            raise Http404
        serializer = ArtistSerializer(farm)
        return Response(serializer.data)
