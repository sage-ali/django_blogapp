from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostDB(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
    ]
    
admin.site.register(Post, PostDB)
admin.site.register(Comment)