from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    blog_image = models.ImageField(upload_to='images/')
    blog_post = models.TextField(default="")
    blog_date = models.DateTimeField(default=timezone.now())
