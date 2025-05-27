from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    post_updated_on = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
