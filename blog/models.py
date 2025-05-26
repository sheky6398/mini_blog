from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300, null=True)
    description = models.TextField()
    post_updated_on = models.DateField(default=timezone.now)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']
