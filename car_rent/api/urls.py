from django.urls import path, include

from .views import CarsViewSet, expired_obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
