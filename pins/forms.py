from django import forms
<<<<<<< HEAD

from .models import Pin
=======
from .models import Pin
from django.db import models
>>>>>>> micah
from django.contrib.admin import widgets


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('pub_date',)
        labels = {
            'pin_room': 'Room: ',
            'pin_description': 'Description',
            'pin_type': 'Type',
<<<<<<< HEAD
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-140 or 200-240 or 300-340'
=======
            'date': 'Date',
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-140 or 200-240 or 300-340',
>>>>>>> micah
            'pin_description': 'please keep descriptions concise',
        }