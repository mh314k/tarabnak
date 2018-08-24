from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from taggit.models import Tag
# Create your views here.
from.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

class BlogPostClassView(ListView):
    model = Post
    queryset = Post.objects.filter(Status='P')
    template_name = "blog/BlogIndex.html"
    paginate_by = 10
    context_object_name = 'Posts'


def taglistview(request, tagname):
    tagg = get_object_or_404(Tag,name=tagname)
    Posts=Post.objects.filter(Tags__in=[tagg])
    paginator = Paginator(Posts,10)
    page = request.GET.get('page')
    try:
        Posts = paginator.get_page(page)
    except PageNotAnInteger:
        Posts=paginator.get_page(paginator.num_pages)
    except EmptyPage:
        Posts=paginator.get_page(1)
    return render(request, 'blog/BlogTagList.html', context={'Posts':Posts, 'tag':tagname, 'paginator':paginator})