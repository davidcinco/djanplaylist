from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Artist, Album, Song

# Create your views here.
def index(request):
    artists = Artist.objects.all()[:3]
    artist_context = {"artists": artists}
    return render(request, "playlist/index.html", artist_context)
        

def artists(request):
    artists = Artist.objects.all()
    artist_context = {"artists": artists}
    return render(request, "playlist/artists.html", artist_context)

def artist(request, id):
    try:
        artist = Artist.objects.get(artistid=id)
        albums = Album.objects.filter(artistfrom=id)

        artist_data = {"artist": artist, "albums": albums}
        return render(request, "playlist/artist.html", artist_data)
    except Exception as e:
        return HttpResponse(e)
    
def album(request, id):
    try:
        album = Album.objects.get(albumid=id)
        # artist = Artist.objects.get(artistid=album.artistfrom.artistid)
        songs = Song.objects.filter(albumfrom=id)

        album_data = {"album": album, "songs": songs}
        return render(request, "playlist/album.html", album_data)

    except Exception as e:
        return HttpResponse(e)
    
def about(request):
    return render(request, "playlist/about.html")