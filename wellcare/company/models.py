from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from pytz import common_timezones

class WellCareUser(User):
    employee_id = models.CharField(max_length=1000,  null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in common_timezones], default='UTC')
    #employee_info = models.ForeignKey('EmployeeInfo', blank=True, null=True)

