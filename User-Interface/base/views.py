from .custom_logic.logic import get_file_size
from django.shortcuts import render
from .models import NexusPassword, File
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Create your views here.
@login_required(login_url="login")
def Home(request):
    context = {'user': request.user}
    return render(request, "base/index.html", context)
@login_required(login_url='login')
def Decrypt(request, webpage, encryption):
    return render(request, 'base/index.html')

@login_required(login_url='login')
def PasswordsPage(request):
    context = {"passwords": NexusPassword.objects.all()}
    return render(request, 'base/passwords.html', context)

@login_required(login_url='login')
def UploadPage(request):
    files = File.objects.all()
    file_sizes = get_file_size(files)
    context = {'items':zip(files, file_sizes)}
    return render(request, 'base/uploads.html', context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def registerUser(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            login(request, user)
            return redirect("home")
        else:
            all_errors = []
            for field, errors in form.errors.items():
                all_errors.extend(errors)
            for error in all_errors:
                messages.error(request, error)
            context = {"formvals": request.POST}
            return render(request, "base/login_register.html", context)
    return render(request, "base/login_register.html", {"form": form})

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")

    context = {"page": page}
    return render(request, "base/login_register.html", context)


@login_required(login_url='login')
def UploadFile(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload-page')
    else:
        form = FileUploadForm()
    context = {'form': form, 'users': User.objects.all()}
    return render(request, 'base/upload_file.html', context)
    

@login_required(login_url='login')
def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_obj.file.name)
        return response

@login_required(login_url='login')
def redirect_404(request, exception):
    return render(request, 'base/404.html', status=404)