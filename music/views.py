from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'music/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'music/home.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def about(request):

    return render(request, 'music/about.html')

def detail(request, id):
    
    return render(request)

