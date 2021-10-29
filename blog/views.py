from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post , BlogComment

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    
    return render(request , "blog/blogHome.html" , context)

def blogPost(request , slug):
    post = get_object_or_404(Post , slug=slug)
    comments = BlogComment.objects.filter(post=post)
    context = {
        "post" : post , 
        "comments" : comments 
    }
    return render(request , "blog/blogPost.html" , context)

# Api for comment
def postComment(request , post_sno):
    if request.method == "POST":
        comment_body = request.POST["comment"] 
        post = Post.objects.get(sno = post_sno)
        user = request.user

        comment = BlogComment(
            comment=comment_body ,
            post=post ,
            user=user
        )
        comment.save()
        messages.success(request , "Your comment has been posted")
        return redirect("BlogPost" , post.slug)
    return redirect("Home")