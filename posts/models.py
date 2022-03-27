from django.db import models
from django.conf import settings


# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

