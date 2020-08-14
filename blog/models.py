from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,"Draft"),(1,"Publish"))

class Wikis(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wiki_posts")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title



# Create your models here.
