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