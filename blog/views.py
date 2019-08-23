from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm, CommentForm


# Create your views here.

# POST ==============================================================
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):

    return


@login_required
def post_publish(request, pk):
    return


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_comment.html', {'form': form})


# Futebol ============================================================
def home(request):
    return render(request, 'blog/home.html')


def championships(request):
    return render(request, 'blog/championships.html')


def stadiums(request):
    return render(request, 'blog/stadiums.html')
