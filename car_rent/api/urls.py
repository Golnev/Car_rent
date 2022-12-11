from django.urls import include, path

from .views import CarsAPIView, CarsAPIUpdate

urlpatterns = [
    path('carlist/', CarsAPIView.as_view()),
    path('carlist/<int:pk>/', CarsAPIUpdate.as_view())
]
