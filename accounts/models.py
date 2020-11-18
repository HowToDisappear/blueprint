import os
import io
import json
from PIL import Image

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile

from gallery.models import Artwork
from events.models import Event
from yourart.models import Yourart
from blueprint.settings import MEDIA_ROOT

IMG_HEIGHT = 190
IMG_WIDTH = 190


# Create your models here.
def user_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    name = instance.user.username
    filename = name + ext
    return f'accounts/{filename}'

def resize(instance):
    f = io.BytesIO()
    img = Image.open(instance.image)
    name = os.path.basename(instance.image.url)
    area = tuple([round(i) for i in json.loads(instance.crop_params)])
    img_crop = img.crop(area)
    img_crop = img_crop.convert('RGB')
    img_crop.thumbnail((IMG_HEIGHT, IMG_WIDTH))
    img.close()
    try:
        img_crop.save(f, format='JPEG')
        s = f.getvalue()
        instance.image.delete()
        instance.save()
        instance.image.save(name, ContentFile(s))
        instance.save()
    finally:
        f.close()


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artworks = models.ManyToManyField(Artwork, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    yourarts = models.ManyToManyField(Yourart, blank=True)
    image = models.ImageField(upload_to=user_path, blank=True, null=True)
    crop = models.BooleanField(default=False)
    crop_params = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.crop == True:
            self.crop = False
            resize(self)
            # if self.image and any((self.image.width > IMG_WIDTH, self.image.height > IMG_HEIGHT)):
            #     resize(self.image.open(), self.crop_params)

    def __str__(self):
        return self.user.username
