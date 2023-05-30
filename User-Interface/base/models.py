from django.db import models

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
    user = models.CharField(max_length=40, default='Sarthak')

class Encryption(models.Model):
    encryption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)