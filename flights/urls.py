from django.urls import path, include
from rest_framework import routers

from flights.views import AirportViewSet

router = routers.DefaultRouter()
router.register("airports", AirportViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "flights"
