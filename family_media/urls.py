from django.urls import path
from . import views

app_name = 'family_media'
urlpatterns = [
    path('family_media/', views.media, name='family_media'),
    path('add_media/', views.add_media, name='add_media'),
]