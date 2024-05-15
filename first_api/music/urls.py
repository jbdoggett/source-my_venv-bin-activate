<<<<<<< Updated upstream
from django.urls import path, include
from rest_framework import routers

from .views import ArtistViewSet, AlbumViewSet, SongViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
=======
# music/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
>>>>>>> Stashed changes
]
