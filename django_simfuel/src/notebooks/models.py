from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage
from django_simfuel.settings import UPLOAD_ROOT

upload_storage = FileSystemStorage(location=UPLOAD_ROOT)

class notebook(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True, null=True,storage=upload_storage)
    notes = JSONField(blank=True, null=True,)
 

