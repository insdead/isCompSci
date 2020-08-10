from django.shortcuts import render
from .models import Post

def blog(request):
    context = {
        'post': Post.objects.all(),
        'title':'Blog'
    }
    return render(request, 'blog/blog.html', context)

def home(request):
    return render(request, 'blog/index.html', {'title':'Home'})

def resume(request):
    return render(request, 'blog/resume.html', {'title':'Resume'})