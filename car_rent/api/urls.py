from django.urls import include, path

from .views import CarsAPIView, CarsAPIDetailView

urlpatterns = [
    path('carlist/', CarsAPIView.as_view()),
    path('carlist/<int:pk>/', CarsAPIDetailView.as_view())
]
