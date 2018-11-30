# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pin(models.Model):
   pin_name = models.CharField(max_length=100)
   pin_description = models.CharField(max_length=300)
   pin_room = models.CharField(max_length=20)
   pub_date = models.DateTimeField('date published')
   
class Vote(models.Model):
   pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
   vote_text = models.CharField(max_length=10)
   votes = models.IntegerField(default=0)