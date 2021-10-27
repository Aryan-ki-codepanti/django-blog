from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

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

