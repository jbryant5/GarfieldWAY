# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_room(pin_room):
   if not (pin_room>100 and pin_room<140):
      raise ValidationError(
         _('%(pin_room)s is not an valid room number'),
            params={'pin_room': pin_room},
        )


TYPE_CHOICES = (
    ('Club', 'Club'),
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Other', 'Other'),
)

# Create your models here.
class Pin(models.Model):
   pin_name = models.CharField(max_length=100)
   pin_description = models.CharField(max_length=300, null = True)
   pin_room = models.CharField(max_length=20, validators = [validate_room])
   pub_date = models.DateTimeField(auto_now_add = True)
   pin_type = models.CharField(choices = TYPE_CHOICES, max_length=10, default='Other', null=True) #pull down for the types of activities
   date = models.DateTimeField()
   def __str__(self):
      return self.pin_name      
   
class Vote(models.Model):
   pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
   vote_text = models.CharField(max_length=10)
   votes = models.IntegerField(default=0)
   def __str__(self):
      return self.vote_text
      