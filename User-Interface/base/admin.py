from django.contrib import admin
from .models import Password, Service, File

# Register your models here.
admin.site.register(File)
admin.site.register(Password)
admin.site.register(Service)
