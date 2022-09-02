from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)
    last_name = models.CharField(blank=False, max_length=100, null=False)
    