from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here

class NexusPassword(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=200)
    password = models.TextField(null = True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self) -> str:
        return self.website
    
class NexusService(models.Model):
    credit = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    webpage = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class File(models.Model):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='uploads/')        
    available_until = models.DateField(default = datetime.date.today() + datetime.timedelta(days=7))
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name
