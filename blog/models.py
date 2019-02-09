from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    blog_image = models.ImageField(upload_to='images/')
    blog_post = models.TextField(default="")
    blog_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def summary(self):
        return self.blog_post[:100]

    def blog_date_pretty(self):
        return self.blog_date.strftime('%b %e %Y %p')
