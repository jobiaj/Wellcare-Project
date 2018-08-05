from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class RoleType(models.Model):
    EMPLOYEE, CLIENT = range(1, 3)
    ROLETYPES = ((EMPLOYEE, 'EMPLOYEE'), (CLIENT, 'CLIENT'))
    name = models.PositiveIntegerField(choices=ROLETYPES, default=EMPLOYEE)

    class Meta:
        app_label = 'company'


class Functions(models.Model):
	name = models.CharField(max_length=100,  null=True, blank=True)
    
    category = models.CharField(max_length=500,  null=True, blank=True)
    function_type = models.ForeignKey('RoleType')
    
    class Meta:
        app_label = 'company'
        unicode_together = ("name", "function_type")

class Role(models.Model):
	name = models.CharField(max_length=100,  null=True, blank=True)
    description = models.CharField(max_length=1000,  null=True, blank=True)
    role_type = models.ForeignKey('RoleType')
    permissions = models.ManyToManyField('Functions')

class UserRoles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.ForeignKey('Role')

class WellCareUser(AbstractUser):
    employee_id = models.CharField(max_length=1000,  null=True, blank=True)
    #employee_info = models.ForeignKey('EmployeeInfo', blank=True, null=True)

