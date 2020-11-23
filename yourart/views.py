import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Yourart, Comment
from .forms import YourartForm

# Create your views here.
def yourart(request):
    qs = Yourart.objects.all()
    return render(request, 'yourart/yourart.html', {'qs': qs})


def artwork(request, artwork):
    artwork_id = int(artwork.split('-')[-1])
    artwork = Yourart.objects.get(id=artwork_id)
    user = request.user
    if request.method == 'POST' and len(request.POST['content']) <= 280 and request.user.is_authenticated:
        comment = Comment(
            artwork=artwork,
            user=user,
            time=datetime.now(),
            content=request.POST['content'],
        )
        comment.save()
    
    comments = Comment.objects.all()
    context = {
        'artwork': artwork,
        'comments': comments,
    }
    return render(request, 'yourart/artwork.html', context)



def submit(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = request.POST.copy()
        data['user'] = request.user
        form = YourartForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/yourart/')
    elif request.method == 'GET':
        form = YourartForm()
    return render(request, 'yourart/submit.html', {'form': form})