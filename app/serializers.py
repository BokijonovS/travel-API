from rest_framework import serializers
from rest_framework.response import Response

from .models import Travel, Car, Hotel


class TravelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    price = serializers.IntegerField()
    car_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()

    def create(self, validated_data):
        return Response(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.car_id = validated_data.get('car_id', instance.car_id)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance


class CarSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Response(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField()
    stars = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Response(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.save()
        return instance
