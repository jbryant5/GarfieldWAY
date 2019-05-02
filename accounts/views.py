from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from pins.models import Pin, Vote
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .forms import RemoveUser
from django.contrib.auth.models import User


def profile(request):
   current_user = request.user
   if current_user.is_authenticated():
      form = SignUpForm(instance=current_user)
      my_pin_list = Pin.objects.filter(user=current_user)
      ordered_my_pin_list = my_pin_list.order_by('-pub_date')
      context = {
         'pin_list': ordered_my_pin_list,
         'form': form,
      }
      template = loader.get_template('profile.html')
   else:
      return redirect('/accounts/login')
   return HttpResponse(template.render(context, request))
#    return render(request, 'profile.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')
            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def deleteAccount (request):
    if request.method == 'POST':
       user = request.user
       user.is_active = False
       user.save()
       return redirect ('/accounts/delete_complete')
    else:
        user = request.user
        template = loader.get_template('deleteAccount.html')
        context = {
           'user':user,
        }
        return HttpResponse(template.render(context, request))

def delete_complete (request):
    if request.method == 'POST':
        return redirect ('/pins')
    else:
        user = request.user
        template = loader.get_template('delete_complete.html')
        context = {
           'user': user,
        }
        return HttpResponse (template.render(context, request))

