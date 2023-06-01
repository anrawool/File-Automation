from django.contrib import admin
from .models import NexusPassword, NexusService, File

# Register your models here.
admin.site.register(File)
admin.site.register(NexusPassword)
admin.site.register(NexusService)
