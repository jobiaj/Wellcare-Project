# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.
def get_login(request,*args, **kwargs):
	if request.method == "POST":
		username = request.POST.get('u',None)
		password = request.POST.get('p',None)
		user = authenticate(username=username, password=password)
		if user is not None:
		    # A backend authenticated the credentials
		    login(request, user)
		    return HttpResponseRedirect(reverse('homepage'))
		else:
		    # No backend authenticated the credentials
			return HttpResponseRedirect(reverse('login'))
	if request.method == "GET":
		return render(request, 'login.html')

@login_required
def get_homepage(request, *args, **kwargs):
	return render(request, 'index.html')

@login_required
def get_contact_info(request, *args, **kwargs):
	return render(request, 'contact.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))