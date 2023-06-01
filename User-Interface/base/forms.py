from .models import File
from django.forms import ModelForm
from django.contrib.auth import get_user_model

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].queryset = get_user_model().objects.exclude(username='admin')
