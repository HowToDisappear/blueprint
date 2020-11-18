from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.art, name='art'),
    path('<author>/<work>', views.artwork, name='artwork'),
    path('<author>', views.artist, name='artist'),
]