from django import forms
from django.forms import Textarea
from .models import Pin
from django import forms
from django.forms import Textarea
from .models import Pin
from django.db import models
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json



class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('pub_date',)
        labels = {
            'pin_name': 'Name ',
            'pin_room': 'Room ',
            'other_pin_room': 'Other Room ',
            'pin_description': 'Description',
            'pin_type': 'Type',
            'date': 'Date',
            'votes':'Up Votes'
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-124 or 200-240 or 300-340 (Optional)',
            'other_pin_room': 'e.g. Gym, Commons, Field (Optional)',
        }
        widgets = {
            'pin_description': Textarea(),
        }

    def clean(self):
        # print(self.cleaned_data)
        # cleaned_data = super(PinForm, self).clean()
        # print("clenaed data: " +  json.dumps(cleaned_data))
        # print("pin room: " + self.cleaned_data["pin_room"])
        pin_room = self.cleaned_data["pin_room"]
        print("pin room: " + pin_room)
        if not (int(pin_room)>100 and int(pin_room)<140):
            print("not valid room")
            raise forms.ValidationError(
                ('%(pin_room)s is not a valid room number'),
                params={'pin_room': pin_room},
            )
        return self.cleaned_data


    # def validate_room():
    #     print ("THE PIN ROOM IS: " + self.pin_room)
        # if not (int(self.pin_room)>100 and int(self.pin_room)<140):
        #     raise ValidationError(
        #         _('%(pin_room)s is not an valid room number'),
        #         params={'pin_room': pin_room},
        #     )
