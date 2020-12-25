# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseNotFound,Http404
from .models import Author, Tag, Category, Post
from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseRedirect, HttpResponsePermanentRedirect
import datetime
from django import template
from django.template import loader



def index(request):
    return HttpResponse('Hello Django')


#view function to display a list of posts

def post_list(request):
    posts = Post.objects.order_by('-id').all()
    return render(request, 'post_list.html',{'posts':posts})


# view function to display a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request,'post_detail.html',{'post': post})

#View function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by('-id') , category = category)
    context = {
        'category' : category,
        'posts' : posts
    }
    print(category)
    return render(request, 'post_by_category.html', context)
#view function to display post by tag

def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    posts = get_list_or_404(Post.objects.order_by('-id'), tags = tag)
    context = {
        'tag' : tag,
        'posts' : posts
    }
    return render(request,'post_by_tag.html',context)

def test_redirect(request):
    return redirect('post_list', permanent=True)