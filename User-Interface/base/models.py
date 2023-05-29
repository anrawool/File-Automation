from django.db import models
from django.http import JsonResponse

# Create your models here

class Password(models.Model):
    website = models.CharField(max_length=200)
    password = models.TextField(null = True, blank=True)
    # user = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.website
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    webpage = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class File(models.Model):
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='uploads/')        

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        
        # Create a new instance of the model
        my_file = File()
        my_file.file.save(uploaded_file.name, uploaded_file)
        my_file.save()
        
        return JsonResponse({'message': 'File uploaded and saved successfully'})
    
    return JsonResponse({'message': 'No file found or invalid request'})
