from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from pytz import common_timezones

class WellCareUser(User):
    employee_id = models.CharField(max_length=1000,  null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in common_timezones], default='UTC')
    employee_info = models.ForeignKey('EmployeeInfo', blank=True, null=True)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=255,  null=True, blank=True)
    address = models.CharField(max_length=255,  null=True, blank=True)
    phoneNumber = models.CharField(max_length=20,  null=True, blank=True)
    MobileNumber = models.CharField(max_length=10,  null=True, blank=True)
    HomePhoneNumber = models.CharField(max_length=10,  null=True, blank=True)
    EmailID = models.CharField(max_length=255,null=True, blank=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    TaxFileName = models.CharField(max_length=255,null=True, blank=True)
    Are_You_Australian_Citizen = models.BooleanField(default=True)
    Do_You_have_working_visa = models.BooleanField(default=True)
    VISA=models.CharField(max_length=255,null=True, blank=True)
    Date_of_Employment = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    Superannuation_Fund_Name = models.CharField(max_length=255,null=True, blank=True)
    CardNumber = models.CharField(max_length=255,null=True, blank=True)
    Expiry_date = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    Registration_Number = models.CharField(max_length=255,null=True, blank=True)
    Comprehensive_insurance = models.BooleanField(default=False)
    Vehicle_Model = models.CharField(max_length=255,null=True, blank=True)
    Bank_name = models.CharField(max_length=255,null=True, blank=True)
    Branch = models.CharField(max_length=255,null=True, blank=True)
    Account_name = models.CharField(max_length=255,null=True, blank=True)
    BSB_number = models.CharField(max_length=255,null=True, blank=True)
    Account_number = models.CharField(max_length=100,null=True, blank=True)
    Contact_name = models.CharField(max_length=255,null=True, blank=True)
    Phone_number = models.CharField(max_length=10,null=True, blank=True)
    Address_of_emergency_contact = models.CharField(max_length=255,null=True, blank=True)
    Employee_signature = models.FileField(upload_to='attachments',null=True, blank=True)
    Date_of_Signature = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    Date_of_Commencement = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    FullTime='FT'
    PartTime='PT'
    Casual='C'
    Employment_Status_Choice = (
        (FullTime,'fulltime'),
        (PartTime,'parttime'),
        (Casual,'casual'),
        )
    Employment_Status = models.CharField(
        max_length=10,
        choices=Employment_Status_Choice,
        default=FullTime,
        )