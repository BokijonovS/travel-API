from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, mixins

from .models import Travel, Car, Hotel
from .serializers import TravelSerializer, CarSerializer, HotelSerializer


# Create your views here.

class TravelAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





    # def get(self, request: Request, pk=None):
    #     if pk is None:
    #         travels = Travel.objects.all()
    #         return Response({'Travels': TravelSerializer(travels, many=True).data})
    #     try:
    #         travel = Travel.objects.get(pk=pk)
    #         return Response({'Travel': TravelSerializer(travel, many=True).data})
    #     except:
    #         return Response({'error': 'Travel not found'})
    #
    # def post(self, request: Request, pk=None):
    #     if pk is None:
    #         travel = TravelSerializer(data=request.data)
    #         travel.is_valid(raise_exception=True)
    #         travel.save()
    #         return Response({'Travel': TravelSerializer(travel, many=True).data, 'message': 'Travel created'})
    #     return Response({'error': 'Travel not found'})
    #
    # def put(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         travel = Travel.objects.get(pk=pk)
    #         return Response({'Travel': TravelSerializer(travel, data=request.data).data})
    #     except:
    #         return Response({'error': 'Travel not found'})
    #
    # def delete(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         travel = Travel.objects.get(pk=pk)
    #         travel.delete()
    #         return Response({'message': 'Travel deleted'})
    #     except:
    #         return Response({'error': 'Travel not found'})

class CarAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request: Request, pk=None):
    #     if pk is None:
    #         cars = Car.objects.all()
    #         return Response({'Cars': CarSerializer(cars, many=True).data})
    #     try:
    #         car = Car.objects.get(pk=pk)
    #         return Response({'Car': CarSerializer(car).data})
    #     except:
    #         return Response({'error': 'Car not found'})
    #
    # def post(self, request: Request, pk=None):
    #     if pk is None:
    #         car = CarSerializer(data=request.data)
    #         car.is_valid(raise_exception=True)
    #         car.save()
    #         return Response({'Car': CarSerializer(car, many=True).data, 'message': 'Cars created'})
    #     return Response({'error': 'Pk should not be provided'})
    #
    # def put(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         car = Car.objects.get(pk=pk)
    #         return Response({'Car': CarSerializer(car, data=request.data).data})
    #     except:
    #         return Response({'error': 'Car not found'})
    #
    # def delete(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         car = Car.objects.get(pk=pk)
    #         car.delete()
    #         return Response({'message': 'Cars deleted'})
    #     except:
    #         return Response({'error': 'Car not found'})

class HotelAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def get(self, request: Request, pk=None):
    #     if pk is None:
    #         hotels = Hotel.objects.all()
    #         return Response({'hotels': HotelSerializer(hotels, many=True).data})
    #     try:
    #         hotel = Hotel.objects.get(pk=pk)
    #         return Response({'hotel': HotelSerializer(hotel).data})
    #     except:
    #         return Response({'error': 'Hotel not found'})
    #
    # def post(self, request: Request, pk=None):
    #     if pk is None:
    #         hotel = HotelSerializer(data=request.data)
    #         hotel.is_valid(raise_exception=True)
    #         hotel.save()
    #         return Response({'Hotel': HotelSerializer(hotel, many=True).data, 'message': 'Hotel created'})
    #
    # def put(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         hotel = Hotel.objects.get(pk=pk)
    #         return Response({'Hotel': HotelSerializer(hotel, data=request.data).data})
    #     except:
    #         return Response({'error': 'Hotel not found'})
    #
    # def delete(self, request: Request, pk=None):
    #     if pk is None:
    #         return Response({'error': 'Pk must be provided'})
    #     try:
    #         hotel = Hotel.objects.get(pk=pk)
    #         hotel.delete()
    #         return Response({'message': 'Hotel deleted'})
    #     except:
    #         return Response({'error': 'Hotel not found'})




