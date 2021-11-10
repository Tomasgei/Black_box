from django.urls import path
from . views import Blog_post_view

urlpatterns = [
    path("",Blog_post_view, name="blog" )
]
