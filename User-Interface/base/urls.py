from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('service/<str:servicename>/', views.GetService, name='service'),
    path('decrypt/<str:webpage>/<str:encryption>/', views.Decrypt, name='decrypt'),
    path('upload/', views.UploadFile, name='upload_file'),
    path('edit-file/<int:file_id>', views.UpdateFile, name='update-file'),
    path('download/<int:file_id>/', views.download_file, name='download'),
]
