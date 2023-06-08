from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.Home, name="home"),
    path('decrypt/<str:webpage>/<str:encryption>/', views.Decrypt, name='decrypt'),
    path('uploads/', views.UploadPage, name='upload-page'),
    path('passwords/', views.PasswordsPage, name='passwords-page'),
    path('upload-file/', views.UploadFile, name='upload-file'),
    path('download/<int:file_id>/', views.download_file, name='download'),
]
