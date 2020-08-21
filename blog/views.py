from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


def blog(request):
    context = {
        'post': Post.objects.all(),
        'title':'Blog'
    }
    return render(request, 'blog/blog.html', context)

def home(request):
    return render(request, 'blog/index.html', {'title':'Home'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
    

def resume(request):
    return render(request, 'blog/resume.html', {'title':'Resume'})

def article(request):
    return render(request, 'blog/article.html', {'title':'Article'})