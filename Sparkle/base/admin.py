from django.contrib import admin

# Register your models here.
from .models import Room, NewsArticle,Message


admin.site.register(Room)
admin.site.register(Message)
admin.site.register(NewsArticle)