from django.http import HttpRequest
from django.views.generic import TemplateView, ListView, DetailView

from .models import Car
from .forms import RentForm
from blog.models import Post


class ContextMixin:
    context = {
        'site_title': ('car', 'book'),
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'instagram': 'https://www.instagram.com/',
        'address': 'Belarus, Minsk',
        'phone': '+375 29 111 11 11',
        'mail': 'email@gmail.com'
    }


class ServicesTemplateView(ContextMixin, TemplateView):
    template_name = 'rent/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesTemplateView, self).get_context_data()
        context.update(self.context)
        return context


class CarListView(ContextMixin, ListView):
    model = Car
    template_name = 'rent/car.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(in_rent=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarListView, self).get_context_data()
        context.update(self.context)
        return context


class CarDetailView(ContextMixin, DetailView):
    model = Car
    template_name = 'rent/car-single.html'
    context_object_name = 'car'
    slug_url_kwarg = 'car_slug'

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data()
        context.update(self.context)
        return context


class MainTemplateView(ContextMixin, TemplateView):
    template_name = 'rent/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainTemplateView, self).get_context_data()
        context.update(self.context)
        context['rent_form'] = RentForm()
        context['cars'] = Car.objects.filter(is_featured=True)
        context['blog'] = Post.objects.order_by('date_published').filter(is_published=True)[:3]
        return context

    def post(self, request: HttpRequest):
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)
