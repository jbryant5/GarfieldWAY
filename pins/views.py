from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import Pin, Vote
from .forms import PinForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.forms.widgets import SelectDateWidget
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
# import schedule
# import time


def index(request):
   buffertime = (timezone.now() - timedelta(days=1))
   passedtime = (timezone.now() - timedelta(days=7))
   upcoming_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('date')
   passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
   context = {
        'pin_list': upcoming_pin_list,
        'old_pin_list': passed_pin_list,
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))
 
def vote(request):
   pin = Pin.objects.get(id=request.GET.get('pin_id'))
   pin.votes += int(request.GET.get('vote'))
   pin.save()
   return redirect('/pins')    

def mypinsfilter(request):
   buffertime = (timezone.now() - timedelta(days=1))
   passedtime = (timezone.now() - timedelta(days=7))
   passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
   current_user = request.user
   if current_user.is_authenticated:
      my_pin_list = Pin.objects.filter(user=request.user, date__gte=buffertime).order_by('-pub_date')
      context = {
        'pin_list': my_pin_list,
        'old_pin_list': passed_pin_list,
      }
      template = loader.get_template('pins/index.html')
      return HttpResponse(template.render(context, request))
   else:
      return redirect('/accounts/login') 

def recentlypublishedfilter(request):
    buffertime = (timezone.now() - timedelta(days=1))
    passedtime = (timezone.now() - timedelta(days=7))
    passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
    latest_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('-pub_date')
    context = {
        'pin_list': latest_pin_list,
        'old_pin_list': passed_pin_list,
    }
    template = loader.get_template('pins/index.html')
    return HttpResponse(template.render(context, request))
    
def oldestpublishedfilter(request):
    buffertime = (timezone.now() - timedelta(days=1))
    passedtime = (timezone.now() - timedelta(days=7))
    passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
    latest_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('pub_date')
    context = {
        'pin_list': latest_pin_list,
        'old_pin_list': passed_pin_list,
    }
    template = loader.get_template('pins/index.html')
    return HttpResponse(template.render(context, request))

def lowestroomfilter(request):
   buffertime = (timezone.now() - timedelta(days=1))
   passedtime = (timezone.now() - timedelta(days=7))
   passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
   room_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('pin_room', 'date')
   context = {
        'pin_list': room_pin_list,
        'old_pin_list': passed_pin_list,
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))
   
def highestroomfilter(request):
   buffertime = (timezone.now() - timedelta(days=1))
   passedtime = (timezone.now() - timedelta(days=7))
   passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
   room_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('-pin_room', 'date')
   context = {
        'pin_list': room_pin_list,
        'old_pin_list': passed_pin_list,
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))

def typefilter(request):
   buffertime = (timezone.now() - timedelta(days=1))
   passedtime = (timezone.now() - timedelta(days=7))
   passed_pin_list = Pin.objects.filter(date__lt=buffertime, date__gte=passedtime).order_by('-date')
   type_pin_list = Pin.objects.filter(date__gte=buffertime).order_by('pin_type', 'date')
   context = {
        'pin_list': type_pin_list,
        'old_pin_list': passed_pin_list,
   }
   template = loader.get_template('pins/index.html')
   return HttpResponse(template.render(context, request))

def create(request):
   current_user = request.user
   if current_user.is_authenticated:
       if request.method == 'GET':
          latest_pin_list = Pin.objects.order_by('-date')
          template = loader.get_template('pins/create.html')
          context = {
              'pin_list': latest_pin_list, 'pin_form': PinForm,
          }
          return HttpResponse(template.render(context, request))
          
       elif request.method == 'POST':
          pin = Pin ()  
          pin.user = current_user
          pin.pin_name = request.POST.get('pin_name')
          pin.pin_room = request.POST.get('pin_room')
          pin.other_pin_room = request.POST.get('other_pin_room')
          pin.pin_description = request.POST.get('pin_description')
          pin.date = request.POST.get('date')
          pin.pin_type = request.POST.get('pin_type')
          pin.save()
          form = PinForm(request.POST, instance=pin)
          if request.POST.get('_save') is not None:
            return redirect('/pins')
          else:
            return redirect('/pins/create')
   else:
      return redirect('/accounts/login')

def edit(request, pin_id):
    pin = get_object_or_404(Pin, pk=pin_id)
    if request.user != pin.user:
      return redirect('/pins')
    if request.method == 'POST':
      form = PinForm(request.POST, instance=pin)
      if form.is_valid():
         pin = form.save(commit=False)
         pin.save()
      if request.POST.get('_save') is not None: 
         pin.pin_name = request.POST.get('pin_name')
         pin.pin_room = request.POST.get('pin_room')
         pin.other_pin_room = request.POST.get('other_pin_room')
         pin.pin_description = request.POST.get('pin_description')
         pin.date = request.POST.get('date')
         pin.pin_type = request.POST.get('pin_type')
         pin.save()
         return redirect('/pins')
    else:
      form = PinForm(instance=pin)
    template = loader.get_template('pins/edit.html')
    context = {
      'pin_form': form,
    }
    return HttpResponse(template.render(context, request))

def delete(request, pin_id):
   pin = get_object_or_404(Pin, pk=pin_id)
   if request.user != pin.user:
      return redirect('/pins')
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

def purge_old_pins (request):
   #  schedule.every().day.at("10:18").do(purge_old_pins(request))
   #  while True:
   #     schedule.run_pending()
   #     #time.sleep(1) 
       now = timezone.now()
       upcoming = Pin.objects.filter(date__gte=now).order_by('date')
       passed = Pin.objects.filter(date__lt=now).order_by('-date')
       if (passed):
          #passed.exclude() hides pins that have passed just while on the purge old pins url
          passed.delete()
       upcoming_pin_list = list(upcoming)
       context = {
          'pin_list': upcoming_pin_list
       }
       template = loader.get_template('pins/index.html')
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
    return HttpResponse("Number of Pins: " + str(numberOfPins))


