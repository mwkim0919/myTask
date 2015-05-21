"""myTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$', 'task.views.home'),
    url(r'^groupview/$', 'task.views.groupview'),
    url(r'^accounts/login/$', 'task.views.login'),
    url(r'^accounts/auth/$', 'task.views.auth_view'),
    url(r'^accounts/loggedin/$', 'task.views.loggedin'),
    url(r'^accounts/invalid_login/$', 'task.views.invalid_login'),
    url(r'^accounts/logout/$', 'task.views.logout'),
    url(r'^accounts/register/$', 'task.views.register_user'),
    url(r'^accounts/register_success/$', 'task.views.register_success'),

    url(r'^admin/', include(admin.site.urls)),
]