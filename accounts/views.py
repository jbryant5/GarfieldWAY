from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('/pins')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
      
     
