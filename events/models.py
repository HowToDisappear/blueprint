from django.db import models
from django.contrib.auth.models import User

from gallery.models import Artist, Artwork


LOC_CHOICES = [
    ('Palace Square, St. Petersburg', 'Palace Square, St. Petersburg'),
    ('Online', 'Online'),
]
ETYPE_CHOICES = [
    ('exhibition', 'Exhibition'),
    ('discussion', 'Discussion'),
    ('workshop', 'Workshop'),
    ('course', 'Course'),
]

class Event(models.Model):
    visitors = models.ManyToManyField(User, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, blank=True, null=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=LOC_CHOICES, default='Palace Square, St. Petersburg')
    etype = models.CharField(max_length=100, choices=ETYPE_CHOICES, default='exhibition')
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    pricem = models.IntegerField(blank=True, null=True)
    descr = models.TextField(max_length=10000, blank=True, null=True)

    class Meta:
        ordering = ['start']

    def __str__(self):
        return self.title
