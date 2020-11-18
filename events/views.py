from datetime import datetime
from datetime import timedelta
from calendar import monthrange

from django.shortcuts import render
from django.db.models import Q

from .models import Event
from .forms import FilterForm


def events(request):
    events = Event.objects.all()
    events_filter = FilterForm(request.GET)
    
    # past events are excluded
    today = datetime.today()
    today = datetime(today.year, today.month, today.day, 23, 59, 59)
    events = events.filter(Q(start__gte=today) | Q(end__gte=today))
    
    etypes = request.GET.get('etypes', '')
    if etypes:
        etypes = etypes.split(',')
        events = events.filter(etype__in=etypes)
    
    location = request.GET.get('location', '')
    if location:
        if location != 'all':
            events = events.filter(location=location)
    
    when = request.GET.get('when', '')
    if when:
        if when == 'tw':
            sooner = today + timedelta(days=6-today.weekday())
            events = events.filter(Q(start__lte=sooner) | Q(end__lte=sooner))
        elif when == 'nw':
            later = today + timedelta(days=6-today.weekday())
            sooner = later + timedelta(days=7)
            events = events.filter(Q(start__gt=later) | Q(end__gt=later),
            Q(start__lte=sooner) | Q(end__lte=sooner))
        elif when == 'tm':
            sooner = datetime(today.year, today.month, monthrange(today.year, today.month)[1])
            events = events.filter(Q(start__lte=sooner) | Q(end__lte=sooner))
        elif when == 'nm':
            later = datetime(today.year, today.month, monthrange(today.year, today.month)[1])
            sooner = later + timedelta(days=monthrange(today.year, today.month+1)[1])
            events = events.filter(Q(start__gt=later) | Q(end__gt=later),
            Q(start__lte=sooner) | Q(end__lte=sooner))
            
    context = {
        'events': events,
        'events_filter': events_filter,
    }
    return render(request, 'events/events.html', context)


def event(request, title):
    event = Event.objects.get(id=title.split('-')[-1])
    return render(request, 'events/event.html', {'ev': event,})