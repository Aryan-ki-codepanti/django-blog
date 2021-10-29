from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post , BlogComment
from blog.templatetags import utils

# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    
    return render(request , "blog/blogHome.html" , context)

def blogPost(request , slug):
    post = get_object_or_404(Post , slug=slug)
    comments = BlogComment.objects.filter(post=post , parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    # Parent ID ----> its replies
    repDict = {}
    for reply in replies:
        if reply.parent.sno in repDict:
            repDict[reply.parent.sno].append(reply)
        else:
            repDict[reply.parent.sno] = [ reply ]

    context = {
        "post" : post , 
        "comments" : comments ,
        "replyDict" : repDict
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

def postReply(request , post_sno , comment_sno):
    if request.method == "POST":
        reply_body = request.POST["reply"] 
        user = request.user
        parent = BlogComment.objects.get(sno=comment_sno)
        post = Post.objects.get(sno=post_sno)
        comment = BlogComment(
            comment=reply_body ,
            parent=parent,
            user=user,
            post=post
        )
        comment.save()
        messages.success(request , "Your reply has been posted")
        return redirect("BlogPost" , post.slug)
    return redirect("Home")