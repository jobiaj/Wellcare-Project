# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
		    WellCareUser = user.wellcareuser
		    return render(request, 'index.html',{'WellCareUser': WellCareUser})
		else:
		    # No backend authenticated the credentials
			return render(request, 'login.html')
	if request.method == "GET":
		return render(request,'login.html')

@login_required
def get_homepage(request, *args, **kwargs):
	return render(request, 'index.html')

