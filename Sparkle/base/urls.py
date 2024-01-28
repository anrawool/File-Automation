from django.urls import path 
from . import views


urlpatterns = [
    path("", views.Home, name='Home'),
    path("room/<str:pk>/", views.room, name='room'),
    # path("add-file/", views.add_file, name='add_file'),
    # path('/login', views.Home, name='Home')
]