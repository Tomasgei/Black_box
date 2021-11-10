from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog_post(models.Model):

    cat_options = (
        ("cat_1","" ),
        ("Trading Systems","Trading Systems" ),
        ("Finance","Finance" ),
        ("News","News" ),
        ("BlackBox","BlackBox" ),
        ("Forex","Forex" ),
        ("Crypto","Crypto" ),
        ("Stocks","Stocks" ),
    )

    options = (
        ("draft", "Draft"),
        ("published","Published"),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 250, unique_for_date = "publish"  )
    publish = models.DateField(default=timezone.now)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default="draft")
    category = models.CharField(max_length=20, choices=cat_options, default="cat_1")

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return str(self.title)



    