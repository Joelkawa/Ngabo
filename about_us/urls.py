from django.urls import path
from . import views

app_name = 'about_us'
urlpatterns = [
    path('about_us/', views.history, name='history'),
    path('about_us/add_history', views.add_history, name='add_history'),
    
]