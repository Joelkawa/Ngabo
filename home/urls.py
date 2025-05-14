from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomePage,name='home'),
    path('posts',views.Posts, name='posts'),
    path('add_post/', views.AddPost, name='add_post'),
    path('family_tree/', views.family_tree, name='family_tree'),
]

