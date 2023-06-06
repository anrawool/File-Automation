from django.shortcuts import render
from .models import NexusPassword, File
from .forms import FileUploadForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

def Home(request):
    return render(request, "base/index.html")


def Decrypt(request, webpage, encryption):
    return render(request, 'base/index.html')

def PasswordsPage(request):
    context = {"passwords": NexusPassword.objects.all()}
    return render(request, 'base/passwords.html', context)

def UploadPage(request):
    context = {'files': File.objects.all()}
    return render(request, 'base/uploads.html', context)


def UploadFile(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload-page')
    else:
        form = FileUploadForm()
    context = {'form': form}
    return render(request, 'base/upload_file.html', context)
    

def UpdateFile(request, file_id):
    file_instance = File.objects.get(id=file_id)
    form = FileUploadForm(instance=file_instance)
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES, instance=file_instance)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/upload_file.html', context)

def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.file.name)
        return response