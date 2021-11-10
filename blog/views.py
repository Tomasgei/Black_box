from django.shortcuts import render,HttpResponse
from . models import Blog_post
# Create your views here.

def Blog_post_view(request):
    posts = Blog_post.objects.all()
    context = {"posts":posts }
    return render(request,"blog/blog_home.html",context)