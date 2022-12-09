from django.forms import ModelForm, TextInput

from .models import Rent


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ('pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date', 'pick_up_time')
        widgets = {
            'pick_up_location': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'City, Airport, Station, etc'
                }
            ),
            'drop_off_location': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'City, Airport, Station, etc'
                }
            ),
            'pick_up_date': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'book_pick_date',
                    'type': 'text',
                    'placeholder': 'Date'
                }
            ),
            'drop_off_date': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'book_off_date',
                    'type': 'text',
                    'placeholder': 'Date'
                }
            ),
            'pick_up_time': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'time_pick',
                    'type': 'text',
                    'placeholder': 'Time'
                }
            )
        }
