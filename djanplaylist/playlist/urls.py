from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists", views.artists, name="artists"),
    path("artist/<int:artistid>", views.artist, name="artist"),
    path("about", views.about, name="about")
]
