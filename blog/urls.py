from django.urls import path
from . views import Blog_post_view, Article_view



urlpatterns = [
    path("",Blog_post_view.as_view(), name="blog" ),
    path("<slug:slug>-<int:pk>/",Article_view.as_view(), name="article_detail" )

] 
