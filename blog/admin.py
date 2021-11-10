from django.contrib import admin
from . import models 

# Register your models here.
class Author_admin(admin.ModelAdmin):
    list_display = ("title","slug","category","publish","status","author")    


admin.site.register(models.Blog_post,Author_admin)