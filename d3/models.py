from django.db import models


class d3(models.Model):
    d3_image = models.ImageField(upload_to='images/')
    d3_summary = models.CharField(max_length=200)
    d3_URL = models.CharField(max_length=50)
