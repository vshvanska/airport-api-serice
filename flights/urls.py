from django.urls import path, include
from rest_framework import routers

from flights.views import (AirportViewSet,
                           CrewViewSet,
                           AirplaneTypeViewSet,
                           RouteViewSet,
                           AirplaneViewSet)


router = routers.DefaultRouter()
router.register("airports", AirportViewSet)
router.register("crews", CrewViewSet)
router.register("airplane_types", AirplaneTypeViewSet)
router.register("routes", RouteViewSet)
router.register("airplanes", AirplaneViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "flights"
