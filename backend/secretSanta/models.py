from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=400)
    createdDate = models.DateTimeField(auto_now_add=True)
    pairingDate = models.DateTimeField(null=True)
    modifiedDate = models.DateTimeField(auto_now=True)

class EventUser(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    isOwner = models.BooleanField(default=False)

class SantaPairing
