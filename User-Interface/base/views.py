from django.shortcuts import render

# Create your views here.
def User(request, email):
    return render(request, "users/login.html")

def Home(request):
    return render(request, "base/index.html")
