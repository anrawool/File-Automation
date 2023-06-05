from django.shortcuts import render
from .models import NexusService, NexusPassword, File
from .forms import FileUploadForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
import os

serviceAvailable = NexusService.objects.all()
# Create your views here.

def Home(request):
    context = {'services': serviceAvailable}
    return render(request, "base/index.html", context)

def GetService(request, servicename):
    if servicename == 'passwords':
        data = NexusPassword.objects.all()
    elif servicename == 'upload':
        response = redirect('/upload/')
        return response
    elif servicename == 'download':
        response = redirect('/download/')
        return response
    else:
        data = NexusService.objects.get(webpage=servicename)
    context = {"data" : data}
    return render(request, f'base/{servicename}.html', context)

def Decrypt(request, webpage, encryption):
    return render(request, 'base/index.html')


def UploadFile(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileUploadForm()
    context = {'form': form, 'files': File.objects.all()}
    return render(request, 'base/upload.html', context)
    
def UpdateFile(request, file_id):
    file_instance = File.objects.get(id=file_id)

    form = FileUploadForm(instance=file_instance)
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, instance=file_instance)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'files':File.objects.all()}

    return render(request, 'base/upload.html', context)

def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.file.name)
        return response