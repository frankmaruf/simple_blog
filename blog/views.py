# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404
from .models import Author, Tag, Category, Post
import datetime
from django import template
from django.template import loader



def index(request):
    return HttpResponse('Hello Django')


#view function to display a list of posts

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})


# view function to display a single post
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post not found")

    return render(request, 'post_detail.html', {'post': post})

#View function to display post by category
def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug = category_slug)
    context = {
        'category' : category,
        'posts' : posts
    }
    print(category)
    return render(request, 'post_by_category.html', context)
#view function to display post by tag

def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag' : tag,
        'posts' : posts
    }
    return render(request,'post_by_tag.html',context)