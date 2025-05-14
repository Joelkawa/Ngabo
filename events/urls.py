from django.urls import path 
from . import views



app_name = 'events'
urlpatterns = [
    path('',views.List_Events, name='list'),
    path('add_event/', views.Add_Event, name='add_event'),
    path('delete_event/<int:event_id>/',views.Delete_Event, name='delete_event')

]
