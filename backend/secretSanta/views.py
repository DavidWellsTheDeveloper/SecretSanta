from rest_framework import viewsets, permissions
# from django_filters import rest_framework as filters
# from secretSanta import filters
from secretSanta import models
from secretSanta import serializers


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MyEventsUserViewSet(viewsets.ModelViewSet):
    # queryset = models.EventUser.objects.all()
    serializer_class = serializers.EventUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.id)
        return models.EventUser.objects.filter(userId=self.request.user.id)

class MyOwnedEventsUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        eventUsers = models.EventUser.objects.filter(userId=self.request.user.id, isOwner=True)
        return models.EventUser.objects.filter(eventId__in=eventUsers.values_list('eventId'))

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