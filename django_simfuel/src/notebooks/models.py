from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

import os
from django_simfuel.settings import MEDIA_ROOT

def content_file_name(instance, filename):
    return os.path.join('notebooks', instance.name, filename)

class notebook(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True, upload_to = content_file_name)
    description = models.TextField(max_length=500, blank =True)
    notes = JSONField(blank=True, null=True)

    def get_edit_url(self):
        return f"/notebooks/{self.pk}"

    def get_delete_url(self):
        return f"/notebooks/{self.pk}/delete/"


    def get_start_url(self):
        return f"/notebooks/{self.pk}/start/"
