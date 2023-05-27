from django.shortcuts import render

# Create your views here.
def Login(request, email):
    context = {'userdata': [{'id': 1, 'email': email}]}
    return render(request, 'users/login.html', context)