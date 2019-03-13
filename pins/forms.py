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
<<<<<<< HEAD
=======

>>>>>>> ec6d0b316442b9cb9875daab84ca6287daee61d0


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

            'pin_room': '100-124 or 200-240 or 300-340',
            
            # 'pin_description': 'please keep descriptions concise',
        }
        widgets = {
            'pin_description': Textarea(),
        }
<<<<<<< HEAD

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password')
=======
#         def __init__(self, *args, **kwargs):
#            super(ShowForm, self).__init__(*args, **kwargs)
#            self.fields['date'].widget = widgets.AdminSplitDateTime()


class SignUpForm(UserCreationForm):
   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email', 'password')
      
      #https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
      #https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
>>>>>>> ec6d0b316442b9cb9875daab84ca6287daee61d0
