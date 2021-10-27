from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    
    return render(request , "blog/blogHome.html" , context)

def blogPost(request , slug):
    context = {
        "slug" : slug
    }
    return render(request , "blog/blogPost.html" , context)