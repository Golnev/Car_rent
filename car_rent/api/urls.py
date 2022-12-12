from django.urls import path, include

from .views import CarsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarsViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('carlist/', CarsViewSet.as_view({'get': 'list'})),
    # path('carlist/<int:pk>/', CarsViewSet.as_view({'put': 'update', 'get': 'retrieve'}))
]
