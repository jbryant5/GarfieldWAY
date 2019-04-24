from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(models.Model):
   username = models.CharField(max_length=100)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   type = models.CharField(max_length =100)
   email = models.CharField(max_length =100)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


