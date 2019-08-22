from django.shortcuts import render

from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


def home(request):
    return render(request, 'blog/home.html')


def championships(request):
    return render(request, 'blog/championships.html')


def stadiums(request):
    return render(request, 'blog/stadiums.html')


# Authorization
"""
def login(request):
    return render(request, 'auth/login.html')
"""
"""
def register(request):
    return render(request, 'auth/register.html')
"""
