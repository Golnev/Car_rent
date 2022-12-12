from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

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


# class CarsAPIUpdate(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# class CarsAPIView(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#
# class CarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


class CarsViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.filter(in_rent=False)
    serializer_class = CarSerializer

    @action(methods=['get'], detail=False)
    def brands(self, request):
        br = Car.objects.all()
        return Response({'brands': set(i.brand for i in br)})
