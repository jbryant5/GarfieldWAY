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
    if request.method == 'GET':
       latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
       template = loader.get_template('pins/create.html')
       context = {
           'latest_pin_list': latest_pin_list,
       }
       return HttpResponse(template.render(context, request))
       
    elif request.method == 'POST':
       pin = Pin ()
       pin.pin_name = request.POST.get('pin_name')
       pin.pin_room = request.POST.get('pin_room')
       pin.pin_description = request.POST.get('pin_description')
       # pin.pub_date = request.POST.get('pub_date_0 +  pub_date_1')
       pin.save()
       return HttpResponse(template.render(context, request))

def test(request):
    test_pin = Pin ()
    test_pin.pin_name = 'test pin!'
    test_pin.pin_room = 105
    test_pin.pin_description = 'this is a test pin'
    test_pin.pub_date = '2018-12-10 09:23:00'
    test_pin.save()
    return HttpResponse ('Test pin')

def getAllRoomPins (request):
    numberOfPins = len(Pin.objects.filter(pin_room = request.GET.get('room')))
    return HttpResponse("Number of Pins: " + str(numberOfPins))



