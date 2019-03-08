# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect

from .models import Pin, Vote
from .forms import PinForm

def index(request):
    latest_pin_list = Pin.objects.order_by('-pub_date')
    context = {
        'pin_list': latest_pin_list
    }
    template = loader.get_template('pins/index.html')
    return HttpResponse(template.render(context, request))
    
def vote(request):
   pin = Pin.objects.get(id=request.GET.get('pin_id'))
   pin.votes += int(request.GET.get('vote'))
   pin.save()
   
   return redirect('/pins')    

def upcomingfilter(request):
   now = timezone.now()
   upcoming = Pin.objects.filter(date__gte=now).order_by('date')
   passed = Pin.objects.filter(date__lt=now).order_by('-date')
   upcoming_pin_list = list(upcoming) + list(passed)
   context = {
        'pin_list': upcoming_pin_list
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))

def roomfilter(request):
   room_pin_list = Pin.objects.order_by('pin_room')
   context = {
        'pin_list': room_pin_list
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))

def typefilter(request):
   type_pin_list = Pin.objects.order_by('pin_type', '-date')
   context = {
        'pin_list': type_pin_list
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'GET':
       latest_pin_list = Pin.objects.order_by('-date')
       template = loader.get_template('pins/create.html')
       context = {
           'pin_list': latest_pin_list, 'pin_form': PinForm,
       }
       return HttpResponse(template.render(context, request))
       
    elif request.method == 'POST':
       pin = Pin ()  
       pin.pin_name = request.POST.get('pin_name')
       pin.pin_room = request.POST.get('pin_room')
       pin.pin_description = request.POST.get('pin_description')
       pin.date = request.POST.get('date')
       pin.pin_type = request.POST.get('pin_type')
       pin.save()
       if request.POST.get('_save') is not None:
         return redirect('/pins')
       else:
         return redirect('/pins/create')

def edit(request, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)
    if request.method == 'POST':
      form = PinForm(request.POST, instance=pin)
      if form.is_valid():
         pin = form.save(commit=False)
         pin.save()
      if request.POST.get('_save') is not None: 
         pin.pin_name = request.POST.get('pin_name')
         pin.pin_room = request.POST.get('pin_room')
         pin.pin_description = request.POST.get('pin_description')
         pin.date = request.POST.get('date')
         pin.pin_type = request.POST.get('pin_type')
         pin.save()
         return redirect('/pins')
#       else:
#          return redirect('/pins/edit/pk')
    else:
      form = PinForm(instance=pin)
    template = loader.get_template('pins/edit.html')
    context = {
      'pin_form': form,
    }
    return HttpResponse(template.render(context, request))

def delete(request, pin_id):
   pin = get_object_or_404(Pin, pk=pin_id)
   if request.method == 'POST':
      form = PinForm(request.POST, instance=pin)
      pin.delete()
      return redirect('/pins')
   else:
      form = PinForm(instance=pin)
   template = loader.get_template('pins/delete.html')
   context = {
      'pin_form': form,
   }
   return HttpResponse(template.render(context, request))


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



