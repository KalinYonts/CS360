from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.

# View for the home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

# View for the post detail page
class PostDetailView(DetailView):
    model = Post
    template_name = 'postDetails.html'

# View for the add post page
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
