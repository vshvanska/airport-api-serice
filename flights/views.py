from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from flights.permissions import IsAdminOrIfAuthenticatedReadOnly
from flights.models import Airport, Crew, AirplaneType, Route, Airplane
from flights.serializers import (AirportSerializer,
                                 CrewSerializer,
                                 AirplaneTypeSerializer,
                                 RouteSerializer,
                                 RouteListSerializer,
                                 RouteRetrieveSerializer,
                                 AirplaneSerializer,
                                 AirplaneListSerializer)


class AirportViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = (IsAdminUser,)


class AirplaneTypeViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = (IsAdminUser,)


class RouteViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Route.objects.all()
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer
        if self.action == "retrieve":
            return RouteRetrieveSerializer
        return RouteSerializer


class AirplaneViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneListSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer
        return AirplaneSerializer
