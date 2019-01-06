from django import forms

from .models import Pin
from django.contrib.admin import widgets


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('pub_date',)
        labels = {
            'pin_room': 'Room: ',
            'pin_description': 'Description',
            'pin_type': 'Type',
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-140 or 200-240 or 300-340'
            'pin_description': 'please keep descriptions concise',
        }