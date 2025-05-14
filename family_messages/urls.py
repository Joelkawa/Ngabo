from django.urls import path
from . import views

app_name = 'family_messages'
urlpatterns = [
   path('',views.Family, name='family'),
   path('message/', views.SendMessage, name='send'),
]