from django.urls import path

from .views import ServicesTemplateView, CarListView, CarDetailView, MainTemplateView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main'),
    path('services/', ServicesTemplateView.as_view(), name='services'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('cars/<slug:car_slug>', CarDetailView.as_view(), name='car')
]
