from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    pairingDate = models.DateTimeField(null=True)
    modifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Name shown by default when refering to this model
        return self.eventName

class EventUser(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    isOwner = models.BooleanField(default=False)
    
    def __str__(self):
        # Name shown by default when refering to this model
        return f"{self.userId.first_name} {self.userId.last_name}: {self.eventId}"

class ExclusionPairing(models.Model):
    id = models.AutoField(primary_key=True)
    eventUser1 = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name="exclusion_user1")
    eventUser2 = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name="exclusion_user2")

class SantaPairing(models.Model):
    id = models.AutoField(primary_key=True)
    santaEventUser = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name="pairing_santa")
    targetEventUser = models.ForeignKey(EventUser, on_delete=models.CASCADE, related_name="pairing_target")

class WishListItem(models.Model):
    id = models.AutoField(primary_key=True)
    eventUser = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    Description = models.TextField()
    url = models.URLField(max_length=500, null=True)
