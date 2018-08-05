from __future__ import unicode_literals

from django.db import models


class ISP(models.Model):
	funding_choices = ['NDIS','Over65','Compensation','Other']
	date = models.DateField()
	review_date = models.DateField()
    full_name = models.CharField(max_length=1000,  null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=1000,  null=True, blank=True)
    funding = models.CharField(choices=funding_choices)
    