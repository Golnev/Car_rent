from datetime import datetime, timedelta

import pytz
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.permissions import IsAdminOrIsAuthenticatedReadOnly
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

class ExpiredTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super(ExpiredTokenAuthentication, self).authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created + timedelta(minutes=2) < utc_now:
            raise AuthenticationFailed('token has expired')
        return user, token


class CarsViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CarsViewSet(ModelViewSet):
    queryset = Car.objects.filter(in_rent=False)
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    pagination_class = CarsViewSetPagination
    authentication_classes = [ExpiredTokenAuthentication]

    @action(methods=['get'], detail=False)
    def brands(self, request):
        br = Car.objects.all()
        return Response({'brands': set(i.brand for i in br)})


class ExpiredObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            pass
        else:
            token.delete()
        token = Token(
            user=user,
        )
        token.save()
        return Response({'token': token.key})


expired_obtain_auth_token = ExpiredObtainAuthToken.as_view()
