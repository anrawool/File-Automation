from django.db import models
import datetime
# Create your models here


class Password(models.Model):
    website = models.CharField(max_length=200)
    password = models.TextField(null = True, blank=True)
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
    user = models.CharField(max_length = 200, default='Sarthak')
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='uploads/')        
    available_until = models.DateField(default = datetime.date.today() + datetime.timedelta(days=7))

    
