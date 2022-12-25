from rest_framework import serializers
from secretSanta import models

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'

class EventUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventUser
        fields = '__all__'

class ExclusionPairingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExclusionPairing
        fields = '__all__'

class SantaPairingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SantaPairing
        fields = '__all__'

class WishListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WishListItem
        fields = '__all__'