from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from pins.models import Pin

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=user.username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/pins')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def delete (request):
    if request.method == 'POST':
        #Pin.objects.filter(username=request.user.username).delete()
        request.user.delete()
        return HttpResponse("Your Account Has Been Deleted.")
    else:
        user = request.user
        template = loader.get_template('deleteAccount.html')
        context = {
           'user':user,
        }
        return HttpResponse(template.render(context, request))