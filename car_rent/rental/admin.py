from django.contrib import admin

from .models import Car, Rent


@admin.action(description='in rent')
def car_in_rent(self, request, queryset):
    queryset.update(in_rent=True)


@admin.action(description='not in rent')
def car_not_in_rent(self, request, queryset):
    queryset.update(in_rent=False)


@admin.action(description='is featured')
def car_is_featured(self, request, queryset):
    queryset.update(is_featured=True)


@admin.action(description='is not featured')
def car_not_is_featured(self, request, queryset):
    queryset.update(is_featured=False)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand', 'model')}
    list_display = ('brand', 'model', 'in_rent', 'price', 'is_featured')
    list_filter = ('is_featured', 'in_rent')
    search_fields = ('brand', 'model', 'price')
    actions = (car_in_rent, car_not_in_rent, car_is_featured, car_not_is_featured)
    fieldsets = (
        (
            'Main options', {
                'fields': ('brand', 'model', 'in_rent', 'price', 'is_featured', 'image'),
                'description': 'Main options'
            }
        ),
        (
            'Additional options', {
                'fields': ('mileage', 'transmission', 'seats', 'luggage', 'fuel', 'description', 'conditioner', 'gps',
                           'child_seat',
                           'trunk', 'music', 'seat_belt', 'sleeping_bed', 'water', 'bluetooth', 'onboard_computer',
                           'audio_input', 'long_term_trips', 'car_kit', 'remote_central_locking', 'climate_control',
                           'slug')
            }
        )
    )


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = (
        'pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date', 'pick_up_time',
        'date_created')
    date_hierarchy = 'date_created'
    search_fields = ('pick_up_date',)
    readonly_fields = (
        'pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date', 'pick_up_time',
        'date_created')
