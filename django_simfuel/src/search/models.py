from django.db import models

# Create your models here.

class Search(models.Model):
    #searchDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.CharField(max_length=120)
    selectedDB = models.CharField(max_length=120)
    search =  models.CharField(max_length=120, blank=True)