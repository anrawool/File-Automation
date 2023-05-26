from django.shortcuts import render

# Create your views here.
def User(request):
    return render(request, "login.html")

def Home(request):
    return render(request, "index.html")
