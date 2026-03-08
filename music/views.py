from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'music/home.html', context)

def about(request):

    return render(request, 'music/about.html')

def detail(request, id):
    
    return render(request)

