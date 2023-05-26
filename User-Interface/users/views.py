from django.shortcuts import render

# Create your views here.
def Login(request, email):
    return render('users/login.html')