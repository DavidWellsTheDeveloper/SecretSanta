from rest_framework import viewsets, permissions
from secretSanta import models
from secretSanta import serializers


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

class EventUserViewSet(viewsets.ModelViewSet):
    queryset = models.EventUser.objects.all()
    serializer_class = serializers.EventUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ExclusionPairingViewSet(viewsets.ModelViewSet):
    queryset = models.ExclusionPairing.objects.all()
    serializer_class = serializers.ExclusionPairingSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SantaPairingViewSet(viewsets.ModelViewSet):
    queryset = models.SantaPairing.objects.all()
    serializer_class = serializers.SantaPairingSerializer
    # permission_classes = [permissions.IsAuthenticated]

class WishListItemViewSet(viewsets.ModelViewSet):
    queryset = models.WishListItem.objects.all()
    serializer_class = serializers.WishListItemSerializer
    # permission_classes = [permissions.IsAuthenticated]