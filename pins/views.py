# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Pin, Vote
from .forms import PinForm

def index(request):
    latest_pin_list = Pin.objects.order_by('-pub_date')[:5]
    context = {
        'latest_pin_list': latest_pin_list
    }
    
    template = loader.get_template('pins/index.html')
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'GET':
       latest_pin_list = Pin.objects.order_by('-date')[:5]
       template = loader.get_template('pins/create.html')
       form = MyForm(request.POST)
       context = {
           'latest_pin_list': latest_pin_list, 'pin_form': PinForm,
       }
       return HttpResponse(template.render(context, request))
       
    elif request.method == 'POST':
       pin = Pin ()  
       pin.pin_name = request.POST.get('pin_name')
       pin.pin_room = request.POST.get('pin_room')
       pin.pin_description = request.POST.get('pin_description')
       pin.date = request.POST.get('date')
       if form.is_valid():
           obj = form.save(commit=False)
           obj.user = request.user
           obj.save()
           return HttpResponseRedirect('obj_list')
       pin.pin_type = request.POST.get('pin_type')
       pin.save()
       if request.POST.get('_save') is not None:
         return redirect('index')
       else:
         return redirect('create')

def clear(request):
    Pin.objects.all().delete()
    return HttpResponse ('Cleared pins')

def test(request):
    test_pin = Pin ()
    test_pin.pin_name = 'test pin!'
    test_pin.pin_room = 105
    test_pin.pin_description = 'this is a test pin'
    test_pin.date = '2018-12-10 09:23:00'
    test_pin.save()
    return HttpResponse('Test pin')
    
def getAllRoomPins (request):
    numberOfPins = len(Pin.objects.filter(pin_room = request.GET.get('room')))
    return HttpResponse("Number of Pins: " + str(numberOfPins))



