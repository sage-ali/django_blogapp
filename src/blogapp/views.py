from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'