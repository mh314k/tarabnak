from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from.models import *

class BlogPostClassView(ListView):
    model = Post
    queryset = Post.objects.filter(Status='P')
    template_name = "blog/List.html"
    paginate_by = 5
    context_object_name = 'Posts'
