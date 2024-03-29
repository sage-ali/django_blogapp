from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])
    
class Comment(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, null=True)
    body = models.TextField(null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, null=True, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'Comment {self.id}'