# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from django import forms


def validate_room (pin_room):
   print ("THE PIN ROOM IS: " + pin_room)
   if not (int(pin_room)>100 and int(pin_room)<140 or (int(pin_room)>=200 and int(pin_room)<240) or (int(pin_room)>=300 and int(pin_room)<340)):
      raise ValidationError(
         _('%(pin_room)s is not a valid room number'),
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
   pin_description = models.CharField(max_length=300, null = True, blank=True)
   pin_room = models.CharField(max_length=20, null=True, blank=True)
   other_pin_room = models.CharField(max_length=100, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   
   def save(self, **kwargs):
      self.clean()
      return super(Pin, self).save(**kwargs)


   pub_date = models.DateTimeField(auto_now_add = True)
   pin_type = models.CharField(choices = TYPE_CHOICES, max_length=10, default='Other', null=True) #pull down for the types of activities
   voters=models.ManyToManyField(User, related_name = 'voters')
   votes=models.IntegerField(default=0)
   date = models.DateTimeField(auto_now_add = False, blank=True)
   user = models.ForeignKey(User, related_name = 'user', on_delete=models.CASCADE)
   
   def __str__(self):
      return self.pin_name      
   
   
