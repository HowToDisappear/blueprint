import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
def user_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    name = '-'.join(instance.title.strip().lower().replace("'","").split(' '))
    filename = name + ext
    return 'yourart/user_{0}/{1}'.format(instance.user.id, filename)

class Yourart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_path)

    def __str__(self):
        return self.title


class Comment(models.Model):
    artwork = models.ForeignKey(Yourart, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField()
    likes = models.IntegerField(default=0)
    content = models.CharField(max_length=280)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.content
