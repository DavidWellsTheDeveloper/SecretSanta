from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=400)
    createdDate = models.DateTimeField(auto_now_add=True)
    pairingDate = models.DateTimeField(null=True)
    modifiedDate = models.DateTimeField(auto_now=True)
