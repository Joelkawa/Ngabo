from django.urls import path
from . import views

app_name = 'ancestry'
urlpatterns = [
    path('ancestry/', views.ancestry, name='ancestry'),
    path('ancestry/endit_ancestry/', views.edit_ancestry, name='edit_ancestry'),
    path('ancestry/add_ancestry/', views.add_ancestry, name='add_ancestry'),


    
]