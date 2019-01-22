from django import forms
from django.forms import Textarea
from .models import Pin
from django.db import models
from django.contrib.admin import widgets


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('pub_date',)
        labels = {
            'pin_name': 'Name ',
            'pin_room': 'Room ',
            'pin_description': 'Description',
            'pin_type': 'Type',
            'date': 'Date',
            'votes':'Up Votes'
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-140 or 200-240 or 300-340',
            # 'pin_description': 'please keep descriptions concise',
        }
        widgets = {
            'pin_description': Textarea(),
        }
#         def __init__(self, *args, **kwargs):
#            super(ShowForm, self).__init__(*args, **kwargs)
#            self.fields['date'].widget = widgets.AdminSplitDateTime()
        