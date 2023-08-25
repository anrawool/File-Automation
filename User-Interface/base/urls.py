from django.urls import path
from . import views
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('', views.Home, name="home"),
    path('decrypt/<str:webpage>/<str:encryption>/', views.Decrypt, name='decrypt'),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('uploads/', views.UploadPage, name='upload-page'),
    path('passwords/', views.PasswordsPage, name='passwords-page'),
    path('upload-file/', views.UploadFile, name='upload-file'),
    path('download/<int:file_id>/', views.download_file, name='download'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'base.views.redirect_404'