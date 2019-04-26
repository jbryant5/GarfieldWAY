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
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .forms import RemoveUser
from django.contrib.auth.models import User


def profile(request):
   current_user = request.user
   if current_user.is_authenticated():
      form = SignUpForm(instance=current_user)
   else:
      return redirect('/accounts/login')
   return render(request, 'profile.html', {'form': form})

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

     
def delete_user(request):
    user = get_object_or_404(User, pk=User_id)
    if request.method == 'POST':
        form = RemoveUser(request.POST)
        if form.is_valid():
            user.delete()
            return redirect('/pins')
        else:
           message = "The account doesn't exist"
    else:
        form = RemoveUser()
    return render(request, 'Remove_User.html', {'form': form})