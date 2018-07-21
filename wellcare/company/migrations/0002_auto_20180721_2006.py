# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-21 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('HomePhoneNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('EmailID', models.CharField(blank=True, max_length=255, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('TaxFileName', models.CharField(blank=True, max_length=255, null=True)),
                ('Are_You_Australian_Citizen', models.BooleanField(default=True)),
                ('Do_You_have_working_visa', models.BooleanField(default=True)),
                ('VISA', models.CharField(blank=True, max_length=255, null=True)),
                ('Date_of_Employment', models.DateField(blank=True, null=True)),
                ('Superannuation_Fund_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('CardNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('Expiry_date', models.DateField(blank=True, null=True)),
                ('Registration_Number', models.CharField(blank=True, max_length=255, null=True)),
                ('Comprehensive_insurance', models.BooleanField(default=False)),
                ('Vehicle_Model', models.CharField(blank=True, max_length=255, null=True)),
                ('Bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Branch', models.CharField(blank=True, max_length=255, null=True)),
                ('Account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('BSB_number', models.CharField(blank=True, max_length=255, null=True)),
                ('Account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('Address_of_emergency_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee_signature', models.FileField(blank=True, null=True, upload_to='attachments')),
                ('Date_of_Signature', models.DateField(blank=True, null=True)),
                ('Date_of_Commencement', models.DateField(blank=True, null=True)),
                ('Employment_Status', models.CharField(choices=[('FT', 'fulltime'), ('PT', 'parttime'), ('C', 'casual')], default='FT', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='wellcareuser',
            name='employee_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.EmployeeInfo'),
        ),
    ]
