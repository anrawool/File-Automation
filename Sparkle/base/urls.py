from django.urls import path 
from . import views


urlpatterns = [
    path("", views.Home, name='Home'),
    path("room/<str:pk>/", views.room, name='room'),
    path("news/", views.news, name='news'),
    path("remove_article/<str:id>", views.remove_article, name='remove-article'),
    path("add_article/<str:id>", views.add_article, name='add-article'),
    # path("add-file/", views.add_file, name='add_file'),
    # path('/login', views.Home, name='Home')
]