from django.contrib import auth
from django.core import serializers
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from forms import RegistrationForm
from models import *
from datetime import datetime


############################
# Main Page
############################


# Rendering the main page '/'
def home(request):
    c = {}
    c.update(csrf(request))
    c['user_authed'] = False
    if request.user.is_authenticated():
        c['user_authed'] = True
    # template = loader.get_template('task/home.html')
    return render_to_response('task/home.html', c)

############################
# Login and Register
############################
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        c = {}
        c.update(csrf(request))
        c.update({'nextURL': request.GET.get('next', '/')})
        return render_to_response('landingPageView.html', c)


def auth_view(request):
    # GET username, if there is no valid data, return ''.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    nextURL = request.POST.get('next', '/dashboard')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(nextURL)
    else:
        return HttpResponseRedirect('/accounts/invalid_login')


def loggedin(request):
    c = {}
    c.update(csrf(request))
    c['username'] = request.user.username
    return HttpResponseRedirect('/dashboard')


def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logout.html')


def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            args['registered'] = True
            return render_to_response('landingPageView.html', args)
        else:
            args['form'] = form
            return render_to_response('landingPageView.html', args)
    args['form'] = RegistrationForm()
    return render(request, 'landingPageView.html', args)