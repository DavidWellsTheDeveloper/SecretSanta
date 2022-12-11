from django.contrib import admin
from secretSanta import models

# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.EventUser)
admin.site.register(models.ExclusionPairing)
admin.site.register(models.SantaPairing)
admin.site.register(models.WishListItem)