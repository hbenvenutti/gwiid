from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def championships(request):
    return render(request, 'blog/championships.html')


def stadiums(request):
    return render(request, 'blog/stadiums.html')


# Authorization

def login(request):
    return render(request, 'auth/login.html')

"""
def register(request):
    return render(request, 'auth/register.html')
"""