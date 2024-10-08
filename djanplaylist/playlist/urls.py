from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists", views.artists, name="artists"),
    path("artist/<int:id>", views.artist, name="artist"),
    path("album/<int:id>", views.album, name="album"),
    path("about", views.about, name="about")
]
