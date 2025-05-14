from django.urls import path
from . import views


app_name = 'custom_messages'
urlpatterns = [
    path('', views.Inbox, name='inbox'),
    path('send_message/',views.Send_Message,name='send'),
    path('send_message/<int:reply_to_id>/', views.Send_Message, name='reply')
]