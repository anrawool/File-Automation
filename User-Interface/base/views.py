from django.shortcuts import render
from .models import Service, Password, File
from .forms import FileUploadForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
import os

serviceAvailable = Service.objects.all()
# Create your views here.

def Home(request):
    context = {'services': serviceAvailable}
    return render(request, "base/index.html", context)

def GetService(request, servicename):
    if servicename == 'passwords':
        data = Password.objects.all()
    elif servicename == 'upload':
        response = redirect('/upload/')
        return response
    elif servicename == 'download':
        response = redirect('/download/')
        return response
    else:
        data = Service.objects.get(webpage=servicename)
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

    return render(request, 'base/upload.html', {'form': form})


def download_file(request, file_id):
    # Retrieve the file object from the database
    file_obj = get_object_or_404(File, id=file_id)

    # Get the file path
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))

    # Open the file
    with open(file_path, 'rb') as file:
        # Set the appropriate response headers
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.file.name)
        return response

def download_page(request):
    context = {'files': File.objects.all()}
    return render(request, 'base/download.html', context)