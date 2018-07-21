# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WellcareUser(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    #avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)