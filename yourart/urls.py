from django.urls import path

from . import views

app_name = 'yourart'
urlpatterns = [
    path('', views.yourart, name='yourart'),
    path('<artwork>', views.artwork, name='artwork'),
    path('submit/', views.submit, name='submit'),
]