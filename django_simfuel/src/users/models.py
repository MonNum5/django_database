from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
from databases. models import database

class userModel(models.Model):
    choices = []
    for i, item in enumerate(database.objects.all()):
        choices.append((item.dbAbbreviation, item.name))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allowedDB = MultiSelectField(choices=choices, blank=True)
