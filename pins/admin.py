# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Pin
from .models import Vote

admin.site.register(Vote)
admin.site.register(Pin)