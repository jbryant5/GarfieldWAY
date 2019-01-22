# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TYPE_CHOICES = (
    ('c', 'Club'),
    ('p', 'Public'),
    ('r', 'Private'),
    ('o', 'Other'),
)

# Create your models here.
class Pin(models.Model):
   pin_name = models.CharField(max_length=100)
   pin_description = models.CharField(max_length=300)
   pin_room = models.CharField(max_length=20)
   pub_date = models.DateTimeField(auto_now_add=True)
   pin_type = models.CharField(max_length=10)
   date = models.DateTimeField()
   type = models.CharField(max_length=1, choices=TYPE_CHOICES)
   votes=models.IntegerField(default=0)
   def __str__(self):
      return self.pin_name
   
class Vote(models.Model):
   pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
   votes = models.IntegerField(default=0)
      