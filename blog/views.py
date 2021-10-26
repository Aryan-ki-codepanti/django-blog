from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("Blog Home")

def blogPost(request , slug):
    return HttpResponse(f"Blog Home { slug } ")