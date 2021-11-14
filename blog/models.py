from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Blog_post(models.Model):

    options = (
        ("draft", "Draft"),
        ("published","Published"),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 255, unique_for_date = "publish", blank = True  )
    publish = models.DateField(default=timezone.now)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default="draft")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    @property
    def get_header_image(self):
        return self.header_image.url

    def get_absolute_url(self):
        kwargs = {"pk": self.id,"slug": self.slug}
        return reverse("article_detail", kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-publish"]
        verbose_name = "Blog Post"

    def __str__(self):
        return str(self.title)
 