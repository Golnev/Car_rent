from rest_framework import serializers
from slugify import slugify
from rental.models import Car


class CarSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.update({'slug': slugify(
            validated_data.get('brand') + '-' + validated_data.get('model'))})
        car = Car(**validated_data)
        car.save()
        return car

    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'image', 'price', 'is_featured', 'description', 'mileage', 'transmission',
                  'seats', 'luggage', 'fuel', 'conditioner', 'gps', 'child_seat', 'trunk', 'music', 'seat_belt',
                  'sleeping_bed', 'water', 'bluetooth', 'onboard_computer', 'audio_input', 'long_term_trips',
                  'car_kit', 'remote_central_locking', 'climate_control')
        # fields = '__all__'
