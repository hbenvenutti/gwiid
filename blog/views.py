from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def championships(request):
    return render(request, 'blog/championships.html')


def stadiums(request):
    return render(request, 'blog/stadiums.html')
