from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    post_updated_on = models.DateField(default=timezone.now)
