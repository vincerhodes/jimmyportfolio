from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    job_summary = models.CharField(max_length=200)
    job_URL = models.CharField(max_length=50)

    def __str__(self):
        return self.job_summary
