from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CarSerializer
from rental.models import Car


# class CarsAPIView(APIView):
#     def get(self, request):
#         c = Car.objects.all()
#         return Response({'cars': CarSerializer(c, many=True).data})
#
#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'car': serializer.data})


class CarsAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsAPIUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
