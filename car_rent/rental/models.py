from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Car(models.Model):
    brand = models.CharField(
        max_length=48,
        verbose_name='car brand'
    )

    model = models.CharField(
        max_length=48,
        verbose_name='car model'
    )

    price = models.IntegerField(
        verbose_name='rent price (day)'
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name='is featured'
    )

    image = models.ImageField(
        upload_to='cars/',
        verbose_name='image',
        default='cars/nophoto.png'
    )

    description = models.TextField(
        verbose_name='description'
    )

    mileage = models.IntegerField(
        verbose_name='mileage'
    )

    transmission = models.CharField(
        max_length=12,
        verbose_name='transmission'
    )

    seats = models.IntegerField(
        verbose_name='seats adults'
    )

    luggage = models.IntegerField(
        verbose_name='luggage bags'
    )

    fuel = models.CharField(
        max_length=12,
        verbose_name='fuel'
    )

    conditioner = models.BooleanField(
        default=True,
        verbose_name='conditioner'
    )

    gps = models.BooleanField(
        default=True,
        verbose_name='gps'
    )

    child_seat = models.BooleanField(
        default=True,
        verbose_name='child seat'
    )

    trunk = models.BooleanField(
        default=True,
        verbose_name='trunk'
    )

    music = models.BooleanField(
        default=True,
        verbose_name='music'
    )

    seat_belt = models.BooleanField(
        default=True,
        verbose_name='seat belt'
    )

    sleeping_bed = models.BooleanField(
        default=True,
        verbose_name='slipping bed'
    )

    water = models.BooleanField(
        default=True,
        verbose_name='water'
    )

    bluetooth = models.BooleanField(
        default=True,
        verbose_name='bluetooth'
    )

    onboard_computer = models.BooleanField(
        default=True,
        verbose_name='onboard computer'
    )

    audio_input = models.BooleanField(
        default=True,
        verbose_name='audio input'
    )

    long_term_trips = models.BooleanField(
        default=True,
        verbose_name='long term trips'
    )

    car_kit = models.BooleanField(
        default=True,
        verbose_name='car kit'
    )

    remote_central_locking = models.BooleanField(
        default=True,
        verbose_name='remote central locking'
    )

    climate_control = models.BooleanField(
        default=True,
        verbose_name='climate control'
    )

    in_rent = models.BooleanField(
        default=False,
        verbose_name='in rent'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    class Meta:
        db_table = 'rental_cars'
        verbose_name = 'car'
        verbose_name_plural = 'cars'
        ordering = ('price',)


class Rent(models.Model):
    pick_up_location = models.CharField(
        max_length=48,
        verbose_name='pick-up location'
    )

    drop_off_location = models.CharField(
        max_length=48,
        verbose_name='pick-off location'
    )

    pick_up_date = models.CharField(
        max_length=48,
        verbose_name='pick-up date'
    )

    drop_off_date = models.CharField(
        max_length=48,
        verbose_name='drop-off date'
    )

    pick_up_time = models.CharField(
        max_length=48,
        verbose_name='pick-up time'
    )

    date_created = models.DateTimeField(
        default=now
    )

    def __str__(self):
        return self.pick_up_date

    class Meta:
        db_table = 'rent_car'
        verbose_name = 'rent'
        verbose_name_plural = 'rents'
        ordering = ('date_created',)
