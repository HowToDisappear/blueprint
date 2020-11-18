from random import sample

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

from .models import Artist, Artwork
from .forms import TestForm, SigninForm


ARTWORKS_RAND = 8

# Create your views here.
def art(request):
    artworks = [sample(list(el.artwork_set.all()), 1)[0] for el in sample(list(Artist.objects.all()), ARTWORKS_RAND)]
    artists = sorted(Artist.objects.all(), key=lambda artist: artist.lname)
    alphabet = sorted({artist.lname[0] for artist in artists})
    alphabet_artists = [(l,[]) for l in alphabet]
    for l in alphabet_artists:
        for a in artists:
            if a.lname[0] == l[0]:
                l[1].append(a)

    context = {
        'artworks': artworks,
        'alphabet_artists': alphabet_artists,
    }
    return render(request, 'gallery/art.html', context)


def artwork(request, author, work):
    fname, lname = [i.capitalize() for i in author.split('-')]
    artwork_id = int(work.split('-')[-1])
    artist_obj = Artist.objects.get(fname=fname, lname=lname)
    artwork_selected = artist_obj.artwork_set.get(id=artwork_id)
    artwork_list = [i for i in artist_obj.artwork_set.all() if i != artwork_selected]

    context = {
        'artwork_selected': artwork_selected,
        'artwork_list': artwork_list,
    }

    return render(request, 'gallery/artwork.html', context)


def artist(request, author):
    fname, lname = [i.capitalize() for i in author.split('-')]
    artist = Artist.objects.get(fname=fname, lname=lname)
    artwork_list = Artwork.objects.filter(artist=artist)
    try:
        event = artist.event_set.all()[0]
    except:
        event = ''
    context = {
        'artist': artist,
        'artwork_list': artwork_list,
        'ev': event,
    }
    return render(request, 'gallery/artist.html', context)
