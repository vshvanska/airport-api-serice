from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from flights.permissions import IsAdminOrIfAuthenticatedReadOnly
from flights.models import Airport, Crew, AirplaneType
from flights.serializers import (AirportSerializer,
                                 CrewSerializer,
                                 AirplaneTypeSerializer)


class AirportViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
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
