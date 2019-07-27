from django.conf import settings
from django.db import models
from django.utils import timezone

class itemList(models.Model):
    username=models.CharField(max_length=128)
    items=models.TextField()