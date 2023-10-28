# from django_filters import rest_framework as filters
from secretSanta import models

class EventUserFilter(filters.FilterSet):
    class Meta:
        model = models.EventUser
        fields = ['userId']