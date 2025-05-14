from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]