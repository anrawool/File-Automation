from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/<str:email>', views.Login, name='login'),
    # path('user/', views.RenderUserInfo, name='userinfo')
]