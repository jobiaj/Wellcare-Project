# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from company.models.usermanagement import RoleType, WellcareUser
# Register your models here.
admin.site.register(RoleType)
admin.site.register(WellcareUser)

