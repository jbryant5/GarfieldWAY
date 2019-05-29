from django import forms

from django.forms import Textarea, DateTimeField, DateField
from .models import Pin
from .widgets import DateTimeLocalWidget, DateTimeLocalField
from django.db import models
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget

from django.forms import Textarea
from .models import Pin
from django.db import models
from django.contrib.admin import widgets
import datetime
import json


class PinForm(forms.ModelForm):
    date = DateTimeLocalField()
    
    class Meta:
        model = Pin
        exclude = ('pub_date', 'user', 'votes','voters')
        labels = {
            'pin_name': 'Name ',
            'pin_room': 'Room ',
            'other_pin_room': 'Other Room ',
            'pin_description': 'Description',
            'pin_type': 'Type',
            'votes':'Up Votes'
            
        }
        help_texts = {
            'pin_room': '100-124 or 200-240 or 300-340 (Optional)',
            'other_pin_room': 'e.g. Gym, Commons, Field (Optional)',
        }
        widgets = {
            'pin_description': Textarea(),
        }

#     def clean(self):
#         # print(self.cleaned_data)
#         # cleaned_data = super(PinForm, self).clean()
#         # print("clenaed data: " +  json.dumps(cleaned_data))
#         # print("pin room: " + self.cleaned_data["pin_room"])
#         pin_room = int(self.cleaned_data["pin_room"])
#         print("pin room: " + str(pin_room))
#         if not((pin_room>=100 and pin_room<124) or (pin_room>=200 and pin_room<240) or (pin_room>=300 and pin_room<340)): 
#             print("not valid room")
#             raise forms.ValidationError(
#                 ('%(pin_room)s is not a valid room number'),
#                 params={'pin_room': pin_room},
#             )
#         return self.cleaned_data


    # def validate_room():
    #     print ("THE PIN ROOM IS: " + self.pin_room)
        # if not (int(self.pin_room)>100 and int(self.pin_room)<140):
        #     raise ValidationError(
        #         _('%(pin_room)s is not an valid room number'),
        #         params={'pin_room': pin_room},
        #     )



class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )