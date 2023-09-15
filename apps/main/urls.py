# Django
from django.urls import path

# Local
from .views import (
    DeleteView,
    DetailView,
    IndexView,
    create_song,
    favorite
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:album_id>/', DetailView.as_view(), name='detail'),
    path('<int:album_id>/create_song/', create_song, name='create_song'),
    path('favorite/<int:song_id>/', FavoriteSongView.as_view(), name='favorite_song'),,
    path(
        '<int:album_id>/delete_song/<int:song_id>/',
        DeleteView.as_view(),
        name='delete_song'
    ),
]
