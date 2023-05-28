from django.contrib import admin

# Register your models here.
from .models import Password, Service, File

admin.site.register(File)
admin.site.register(Password)
admin.site.register(Service)