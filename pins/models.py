# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_room (pin_room):
   print ("THE PIN ROOM IS: " + pin_room)
   if not (pin_room>100 and pin_room<140):
      raise ValidationError(
         _('%(pin_room)s is not an valid room number'),
            params={'pin_room': pin_room},
        )

TYPE_CHOICES = (
    ('c', 'Club'),
    ('p', 'Public'),
    ('r', 'Private'),
    ('o', 'Other'),
)
# Create your models here.
class Pin(models.Model):
   pin_name = models.CharField(max_length=100)
   pin_description = models.CharField(max_length=300, null = True)
   pin_room = models.CharField(max_length=20, validators = [validate_room])
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   
   def save(self, **kwargs):
      self.clean()
      print ('The form is saving')
      return super(Pin, self).save(**kwargs)

   def clean (self):
      pin_number = int(self.pin_room)
      print(self.pin_room)
      if not((pin_number>100 and pin_number<124) or (pin_number>200 and pin_number<240) or (pin_number>300 and pin_number<340)): 
         raise ValidationError ('Please enter a valid room number')
      elif():
         return self.pin_room


   pub_date = models.DateTimeField(auto_now_add = True)
   pin_type = models.CharField(choices = TYPE_CHOICES, max_length=1) #pull down for the types of activities
   date = models.DateTimeField()
   def __str__(self):
      return self.pin_name
   
class Vote(models.Model):
   pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
   vote_text = models.CharField(max_length=10)
   votes = models.IntegerField(default=0)
   def __str__(self):
      return self.vote_text
      