from .models import *
from django.forms import ModelForm

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['owner', 'name', 'file'] 
    

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "profile_pic", "phone_number"]
