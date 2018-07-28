# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from forms import UserInfoForm
from models import WellCareUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_login(request,*args, **kwargs):
	if request.method == "POST":
		username = request.POST.get('u',None)
		password = request.POST.get('p',None)
		user = WellCareUser.objects.get(username=username, password=password)
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
	user = WellCareUser.objects.get(id=request.user.id)
	user_info = WellCareUser.objects.get(id=request.user.id).employee_info
	user_info_available = False
	if user_info:
		user_info_available = True
	data = {'user_info_available': user_info_available, 'user_info': user_info}
	return render(request, 'index.html', data)

@login_required
def get_contact_info(request, *args, **kwargs):
	return render(request, 'contact.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

@login_required
@csrf_exempt
def add_user_informations(request, user_id):
	form = UserInfoForm()
	extra = None
	if request.method == 'POST':
		form = UserInfoForm(request.POST)

		if form.is_valid():
			try:
				user = WellCareUser.objects.get(id=user_id)
				user_info = form.save()
				user.add_user_info(user_info)
			except Exception as e:
				extra = 'Error occured during adding user info %s' %str(e)
				res = {'status': status, 'complete': False, 'tmpl': tmpl, 'extra': extra}
				return HttpResponse(json.dumps(res), content_type='application/json')
			else:
				data = {'user_info_available': True, 'user_info': user_info}
				return render(request, 'index.html', data)
	for bound_field in form:
		bound_field.field.widget.attrs.update({'class': 'form-control'})

	tmpl = render_to_string('partials/user_info.html', {'form': form}, request)
	status = False if extra else True
	res = {'status': status, 'complete': False, 'tmpl': tmpl, 'extra': extra}
	return HttpResponse(json.dumps(res), content_type='application/json')