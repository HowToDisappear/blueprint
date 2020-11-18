from django.db import models

# Create your models here.

class Artist(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    born = models.PositiveIntegerField()
    died = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(max_length=10000, blank=True, null=True)
    wiki = models.CharField(max_length=130, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ymade = models.PositiveIntegerField()
    medium = models.CharField(max_length=100)
    descr = models.TextField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return self.title
