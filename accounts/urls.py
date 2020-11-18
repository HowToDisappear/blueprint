from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('activate/<uid>/<token>', views.activate, name='activate'),
    path('<account>', views.account, name='account'),
]
