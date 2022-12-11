from django.urls import path, include
from rest_framework.routers import DefaultRouter
from secretSanta import views

from . import views

router = DefaultRouter()
router.register(r'event', views.EventViewSet, basename="event")
router.register(r'eventUser', views.EventUserViewSet, basename="eventUser")
router.register(r'exclusionPairing', views.ExclusionPairingViewSet, basename="exclusionPairing")
router.register(r'santaPairing', views.SantaPairingViewSet, basename="santaPairing")
router.register(r'wishListItem', views.WishListItemViewSet, basename="wishListItem")

urlpatterns = [
    path('', include(router.urls)),
]