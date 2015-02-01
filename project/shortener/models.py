from django.db import models

class URL(models.Model):
  short_id = models.CharField(max_length=8, unique=True)
  full_URL = models.CharField(max_length=2048)
