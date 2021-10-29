from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate  , login , logout

# Create your views here.

# HTML Pages
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
    if q == "" or len(q) > 78 or not posts:
        context["posts"] = []
        messages.warning(request , "No results found")
        return render(request , "base/search.html" , context)
    return render(request , "base/search.html" , context)

# Authentication
def handleSignUp(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        # Refine data
        if  not username.isalnum():
            messages.error(request , "Username must be alphanumeric")
            return redirect("Home")
        if  len(username) < 10:
            messages.error(request , "Username must be between 0 and 10 character")
            return redirect("Home")
        if  password != cpassword:
            messages.error(request , "Passwords do not match")
            return redirect("Home")
        

        # Save user
        user = User(
                username=username,
                first_name=fname,
                last_name=lname,
                password=password,
                email=email
            )

        user.save()
        messages.success(request , "Your iCoder account has been successfully created")


        return redirect("Home")

    return HttpResponse("404 not Found")

def handleLogin(request):

    if request.method == "POST":
        username = request.POST["login-username"]
        password = request.POST["login-password"]

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request , user)
            messages.success(request , "You have been logged in")
            return redirect("Home")
        messages.error(request , "Invalid login credentials , try again")
        return redirect("Home")

    return HttpResponse("404 not Found")

def handleLogout(request):
    logout(request)
    messages.success(request , "Successfully logged out")
    return redirect("Home")
