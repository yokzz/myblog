from django.db import models
from django.utils import timezone
from datetime import timedelta

class Author(models.Model):
    name = models.CharField(max_length=63)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name='post',
                               default=None)
    
    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author_name = models.CharField(max_length=63)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='comments',
                             default=None)
    
    def __str__(self):
        return self.text