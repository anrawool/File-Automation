from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('user/', views.User, name='user'),
]
