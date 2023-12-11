from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from flights.models import Airport, Crew, AirplaneType, Ticket, Route


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name")


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ("id", "source", "destination", "distance")


class RouteListSerializer(RouteSerializer):
    source = serializers.CharField(
        source="source.closest_big_city", read_only=True
    )
    destination = serializers.CharField(
        source="destination.closest_big_city", read_only=True
    )

    class Meta:
        model = Route
        fields = ("id", "source", "destination", "distance")


class RouteRetrieveSerializer(RouteSerializer):
    source = AirportSerializer(read_only=True)
    destination = AirportSerializer(read_only=True)


class TicketSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs=attrs)
        Ticket.validate_ticket(
            attrs["row"],
            attrs["seat"],
            attrs["movie_session"].cinema_hall,
            ValidationError,
        )
        return data
