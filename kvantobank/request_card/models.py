from statistics import mode
from django.db import models

class ScanedCard(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)