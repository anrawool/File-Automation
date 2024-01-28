from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
def Home(request):
    context = {'rooms': Room.objects.all()}
    return render(request, 'index.html', context)



def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

