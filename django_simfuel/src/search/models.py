from django.db import models

from django.utils.timezone import now

# Create your models here.

class Search(models.Model):
    searchDate=models.DateTimeField(default=now)
    user = models.CharField(max_length=120, blank=True)
    selectedDB = models.CharField(max_length=120, blank=True)
    search =  models.CharField(max_length=120, blank=True)