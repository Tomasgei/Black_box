from django.shortcuts import render,HttpResponse
from . models import Blog_post
from django.views.generic import DetailView, TemplateView, ListView
from tradingapp.models import User_profile
# Create your views here.
""" FBV
def Blog_post_view(request):
    posts = Blog_post.objects.all()
    context = {"posts":posts }
    return render(request,"blog/blog_home.html",context)
"""

class Blog_post_view(TemplateView):

    template_name = "blog/blog_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Blog_post.objects.all()
        return context
    

class Article_view(DetailView):
    model = Blog_post
    template_name = "blog/blog_detail.html"
    context_object_name = "blog_post"
