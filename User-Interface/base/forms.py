from .models import File
from django.forms import ModelForm

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['owner', 'name', 'file'] 
    
