from django.urls import path

from . import views

urlpatterns = [
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistView.as_view(), name='artist'),

    path('albums/', views.AlbumListView.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumView.as_view(), name='album'),

    path('artists/albums/', views.ArtistAlbumsListView.as_view(), name='artist-albums-list'),
    path('artists/<int:pk>/albums/', views.ArtistAlbumsView.as_view(), name='artist-albums'),
]
