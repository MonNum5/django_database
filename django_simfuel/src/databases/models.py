from django.db import models

# Create your models here.

import os
from django_simfuel.settings import MEDIA_ROOT
def content_file_name(instance, filename):
    return os.path.join('images/databaseImages', filename)


class database(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    dbAbbreviation = models.CharField(max_length=10, blank=False, unique=True)
    description = models.TextField(max_length=120, blank=True)
    image =  models.FileField(
    default = os.path.join('images/databaseImages', 'defaultDBImage.png'), upload_to = content_file_name)

    def get_edit_url(self):
        return f"/databases/{self.pk}"

    def get_delete_url(self):
        return f"/databases/{self.pk}/delete/"

    

