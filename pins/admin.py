# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Pin
from .models import Vote

def make_club(modeladmin, request, queryset):
   queryset.update(status='c')
make_club.short_description="Mark events as club events"
def make_public(modeladmin, request, queryset):
   queryset.update(status='p')
make_public.short_description="Mark events as public events"


class PinAdmin(admin.ModelAdmin):
    list_display = ['pin_name', 'pin_type']
    ordering = ['pub_date']
    actions = [make_club, make_public]

admin.site.register(Vote)
admin.site.register(Pin, PinAdmin)