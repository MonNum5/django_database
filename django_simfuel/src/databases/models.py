from django.db import models

# Create your models here.

class database(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)
    dbAbbreviation = models.CharField(max_length=10, blank=False, unique=True)
    description = models.TextField(max_length=120, blank=True)
    image =  models.ImageField(blank=True, null=True, default = 'defaultDBImage.png')

    def get_edit_url(self):
        return f"/databases/{self.pk}"

    def get_delete_url(self):
        return f"/databases/{self.pk}/delete/"

    

