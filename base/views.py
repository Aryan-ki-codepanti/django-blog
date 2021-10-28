from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    return render(request , "base/home.html")

def about(request):
    return render(request , "base/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        

        # check blank
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 5:
            messages.error(request , "Fill form correctly")
        else:
            contact = Contact(
                name=name , 
                email=email,
                phone=phone,
                content=content
                )
            messages.success(request , "Your message has been sent")
            contact.save()
        return redirect("Contact")
    return render(request , "base/contact.html")

def search(request):
    q = request.GET['q'] if request.GET['q'] else ""

    posts = Post.objects.filter(
        Q(title__icontains=q) | 
        Q(content__icontains=q) | 
        Q(author__icontains=q)  
    )
    context = {
        "q": q , 
        "posts" : posts
    }
    return render(request , "base/search.html" , context)