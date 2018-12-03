# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Pin, Vote

def index(request):
    latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
    template = loader.get_template('pins/index.html')
    context = {
        'latest_pin_list': latest_pin_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
    template = loader.get_template('pins/create.html')
    context = {
        'latest_pin_list': latest_pin_list,
    }
    return HttpResponse(template.render(context, request))