from django.shortcuts import render
from .models import Service, Password, File
from .forms import FileUploadForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
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
    if request.method == 'POST' and request.FILES.get('file') and request.POST.get('name'):
        file = request.FILES['file']
        name = request.POST['name']
        file_path = os.path.join('../media/uploads/', file.name)
        
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Save the name and file_path to your model or perform other actions
        
        return HttpResponse('File uploaded successfully.')
    
    return HttpResponse('No file or invalid request.')



def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.file.name)
        return response