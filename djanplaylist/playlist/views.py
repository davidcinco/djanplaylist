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

def artist(request, artistid):
    try:
        artist = Artist.objects.get(artistid=artistid)
        return HttpResponse(artist.artistname)
    #     # return render(request, "playlist/index.html", context)
    #     return context
    except Exception as e:
        return HttpResponse(e)
    
def about(request):
    return render(request, "playlist/about.html")