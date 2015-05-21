from django.contrib import auth
from django.core import serializers
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext

from forms import RegistrationForm
from models import *
from datetime import datetime

# The Intro Page
def home(request):
    # c = {}
    return render(request, 'task/home.html')

def groupview(request):
    if request.user.is_authenticated():
        return render(request, 'task/groupview.html')
    else:
        return HttpResponseRedirect('/accounts/login')

############################
# Login and Register
############################

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('task/account/login.html', c)

def auth_view(request):
    # GET username or if there is no valid data, return ''.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid_login')

def loggedin(request):
    c = {}
    c.update(csrf(request))
    c['username'] = request.user.username
    test = request.POST.get('title', '')
    return HttpResponseRedirect('/groupview')

def invalid_login(request):
    return render_to_response('task/account/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('task/account/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('task/account/register.html', {'form': form})
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'task/account/register.html', args)

def register_success(request):
    return render_to_response('task/account/register_success.html')