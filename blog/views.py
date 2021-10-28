from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    
    return render(request , "blog/blogHome.html" , context)

def blogPost(request , slug):
    post = get_object_or_404(Post , slug=slug)
    print(post)
    context = {
        "post" : post 
    }
    return render(request , "blog/blogPost.html" , context)