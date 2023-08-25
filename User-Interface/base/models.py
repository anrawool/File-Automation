from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from .managers import UserManager
# Create your models here


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, editable=True)
    email = models.EmailField(max_length=100, unique=True, editable=True)
    profile_pic = models.ImageField(null=True, blank=True, default="./profile_pics/default_pic.png", upload_to='./profile_pics/')
    phone_number = models.IntegerField(unique=True, null=True)
    emergency_contact = models.IntegerField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'emergency_contact']

    objects = UserManager() 

    def __str__(self):
        return self.username

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
    
class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='uploads/')        
    available_until = models.DateField(default = datetime.date.today() + datetime.timedelta(days=7))
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name
