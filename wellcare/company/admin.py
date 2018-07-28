# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import WellCareUser, EmployeeInfo,ISP, Representative, ServiceType, Daily_routine, General, Medicle, PersonalCare, Mobility, Equipment_and_aids, Behaviour, Household_tasks, Transport
admin.site.register(WellCareUser)
admin.site.register(EmployeeInfo)
admin.site.register(ISP)
admin.site.register(Representative)
admin.site.register(ServiceType)
admin.site.register(Daily_routine)
admin.site.register(General)
admin.site.register(Medicle)
admin.site.register(PersonalCare)
admin.site.register(Mobility)
admin.site.register(Equipment_and_aids)
admin.site.register(Behaviour)
admin.site.register(Household_tasks)
admin.site.register(Transport)

