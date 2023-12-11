from django.urls import path, include
from rest_framework import routers

from flights.views import (AirportViewSet,
                           CrewViewSet,
                           AirplaneTypeViewSet,
                           RouteViewSet)


router = routers.DefaultRouter()
router.register("airports", AirportViewSet)
router.register("crews", CrewViewSet)
router.register("airplane_types", AirplaneTypeViewSet, basename='airplanetype')
router.register("routes", RouteViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "flights"
