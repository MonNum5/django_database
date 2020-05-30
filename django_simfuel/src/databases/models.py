from django.db import models

# Create your models here.

class database(models.Model):
    name = models.CharField(max_length=120, blank=True)
    dbAbbreviation = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=120, blank=True)
    image =  models.ImageField(blank=True, null=True)