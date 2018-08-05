# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_merge_20180729_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allergy', models.BooleanField(default=True)),
                ('NIL', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Behavior_management', models.BooleanField(default=True)),
                ('Details_Behavior_management', models.CharField(blank=True, max_length=1000, null=True)),
                ('Community_support', models.BooleanField(default=True)),
                ('Details_Community_support', models.CharField(blank=True, max_length=1000, null=True)),
                ('Supervision', models.BooleanField(default=True)),
                ('Details_Supervision', models.CharField(blank=True, max_length=1000, null=True)),
                ('Time_management', models.BooleanField(default=True)),
                ('Details_Time_management', models.CharField(blank=True, max_length=1000, null=True)),
                ('Transport_or_vehicle', models.BooleanField(default=True)),
                ('Details_Transport_or_vehicle', models.CharField(blank=True, max_length=1000, null=True)),
                ('Triggers', models.BooleanField(default=True)),
                ('Details_Triggers', models.CharField(blank=True, max_length=1000, null=True)),
                ('Communication', models.BooleanField(default=True)),
                ('Details_Communication', models.CharField(blank=True, max_length=1000, null=True)),
                ('Routine', models.BooleanField(default=True)),
                ('Details_Routine', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Morning_routine', models.BooleanField(default=True)),
                ('Details_Morning_routine', models.CharField(blank=True, max_length=1000, null=True)),
                ('Afternoon_routine', models.BooleanField(default=True)),
                ('Details_Afternoon_routine', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bed_time_routine', models.BooleanField(default=True)),
                ('Details_Bed_time_routine', models.CharField(blank=True, max_length=1000, null=True)),
                ('General_daily_routine', models.BooleanField(default=True)),
                ('Details_General_daily_routine', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_and_aids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_or_aids_required', models.BooleanField(default=True)),
                ('Details_Equipment_or_aids_required', models.CharField(blank=True, max_length=1000, null=True)),
                ('Wheel_chair', models.BooleanField(default=True)),
                ('Details_Wheel_chair', models.CharField(blank=True, max_length=1000, null=True)),
                ('Walking_frame_stick', models.BooleanField(default=True)),
                ('Details_Walking_frame_stick', models.CharField(blank=True, max_length=1000, null=True)),
                ('Shower_chair', models.BooleanField(default=True)),
                ('Details_Shower_chair', models.CharField(blank=True, max_length=1000, null=True)),
                ('Communication', models.BooleanField(default=True)),
                ('Details_Communication', models.CharField(blank=True, max_length=1000, null=True)),
                ('Assistive_technology', models.BooleanField(default=True)),
                ('Details_Assistive_technology', models.CharField(blank=True, max_length=1000, null=True)),
                ('Maintenance_of_equipment', models.BooleanField(default=True)),
                ('Details_Maintenance_of_equipment', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Communication', models.BooleanField(default=False)),
                ('Details_Communication', models.CharField(blank=True, max_length=1000, null=True)),
                ('Decision_making', models.BooleanField(default=False)),
                ('Details_Decision_making', models.CharField(blank=True, max_length=1000, null=True)),
                ('Cultural_background', models.BooleanField(default=True)),
                ('Details_Cultural_background', models.CharField(blank=True, max_length=1000, null=True)),
                ('Language', models.BooleanField(default=True)),
                ('Details_Language', models.CharField(blank=True, max_length=1000, null=True)),
                ('Nutrition_or_diet_or_weight', models.BooleanField(default=True)),
                ('Details_Nutrition_or_diet_or_weight', models.CharField(blank=True, max_length=1000, null=True)),
                ('Vision', models.BooleanField(default=True)),
                ('Details_Vision', models.CharField(blank=True, max_length=1000, null=True)),
                ('Hearing', models.BooleanField(default=True)),
                ('Details_Hearing', models.CharField(blank=True, max_length=1000, null=True)),
                ('Speech', models.BooleanField(default=True)),
                ('Details_Speech', models.CharField(blank=True, max_length=1000, null=True)),
                ('Financial_or_money', models.BooleanField(default=True)),
                ('Details_Financial_or_money', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Household_tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shopping', models.BooleanField(default=True)),
                ('Details_Shopping', models.CharField(blank=True, max_length=1000, null=True)),
                ('Kitchen_or_meal_preparation', models.BooleanField(default=True)),
                ('Details_Kitchen_or_meal_preparation', models.CharField(blank=True, max_length=1000, null=True)),
                ('Laundry', models.BooleanField(default=True)),
                ('Details_Laundry', models.CharField(blank=True, max_length=1000, null=True)),
                ('Cleaning_or_room_maintenance', models.BooleanField(default=True)),
                ('Details_Cleaning_or_room_maintenance', models.CharField(blank=True, max_length=1000, null=True)),
                ('Gardening', models.BooleanField(default=True)),
                ('Details_Gardening', models.CharField(blank=True, max_length=1000, null=True)),
                ('Pet_or_animal_care', models.BooleanField(default=True)),
                ('Details_Pet_or_animal_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Phone_or_mail_or_computer', models.BooleanField(default=True)),
                ('Details_Phone_or_mail_or_computer', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medication_documentation', models.BooleanField(default=True)),
                ('Details_Medication_documentation', models.CharField(blank=True, max_length=1000, null=True)),
                ('Medication', models.BooleanField(default=True)),
                ('Details_Medication', models.CharField(blank=True, max_length=1000, null=True)),
                ('Medical_conditions', models.BooleanField(default=True)),
                ('Details_Medical_conditions', models.CharField(blank=True, max_length=1000, null=True)),
                ('Seizure_management_plan', models.BooleanField(default=True)),
                ('Details_Seizure_management_plan', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bowel_management_plan', models.BooleanField(default=True)),
                ('Details_Bowel_management_plan', models.CharField(blank=True, max_length=1000, null=True)),
                ('PEG', models.BooleanField(default=True)),
                ('Details_PEG', models.CharField(blank=True, max_length=1000, null=True)),
                ('Infectious_diseases', models.BooleanField(default=True)),
                ('Has_Client_had_chicken_fox', models.BooleanField(default=True)),
                ('Has_Client_had_Hepatitis_A_B_C_orD', models.BooleanField(default=True)),
                ('Immunization', models.BooleanField(default=True)),
                ('Triple_antigen_Date', models.BooleanField(default=True)),
                ('Sabin_Date', models.BooleanField(default=True)),
                ('TetanusDate', models.BooleanField(default=True)),
                ('Medical_appointments', models.BooleanField(default=True)),
                ('Details_Medical_appointments', models.CharField(blank=True, max_length=1000, null=True)),
                ('Advanced_care_plan', models.BooleanField(default=True)),
                ('Details_Advanced_care_plan', models.CharField(blank=True, max_length=1000, null=True)),
                ('Nursing_support', models.BooleanField(default=True)),
                ('Details_Nursing_support', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weight_bear', models.BooleanField(default=True)),
                ('Details_Weight_bear', models.CharField(blank=True, max_length=1000, null=True)),
                ('Stand_transfer', models.BooleanField(default=True)),
                ('Details_Stand_transfer', models.CharField(blank=True, max_length=1000, null=True)),
                ('Hoist_transfer', models.BooleanField(default=True)),
                ('Details_Hoist_transfer', models.CharField(blank=True, max_length=1000, null=True)),
                ('Walking_or_running', models.BooleanField(default=True)),
                ('Details_Walking_or_running', models.CharField(blank=True, max_length=1000, null=True)),
                ('Positioning', models.BooleanField(default=True)),
                ('Details_Positioning', models.CharField(blank=True, max_length=1000, null=True)),
                ('Exercise', models.BooleanField(default=True)),
                ('Details_Exercise', models.CharField(blank=True, max_length=1000, null=True)),
                ('WHS_issues_or_manual_handling', models.BooleanField(default=True)),
                ('Details_WHS_issues_or_manual_handling', models.CharField(blank=True, max_length=1000, null=True)),
                ('Wheel_chair', models.BooleanField(default=True)),
                ('Details_Wheel_chair', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hygiene', models.BooleanField(default=True)),
                ('Details_Hygiene', models.CharField(blank=True, max_length=1000, null=True)),
                ('Pressure_care', models.BooleanField(default=True)),
                ('Details_Pressure_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bladder_care', models.BooleanField(default=True)),
                ('Details_Bladder_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bowel_care', models.BooleanField(default=True)),
                ('Details_Bowel_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Toileting', models.BooleanField(default=True)),
                ('Details_Toileting', models.CharField(blank=True, max_length=1000, null=True)),
                ('Menstrual_management', models.BooleanField(default=True)),
                ('Details_Menstrual_management', models.CharField(blank=True, max_length=1000, null=True)),
                ('Positioning', models.BooleanField(default=True)),
                ('Details_Positioning', models.CharField(blank=True, max_length=1000, null=True)),
                ('Meal_assistance', models.BooleanField(default=True)),
                ('Details_Meal_assistance', models.CharField(blank=True, max_length=1000, null=True)),
                ('Oral_care', models.BooleanField(default=True)),
                ('Details_Oral_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Bath_or_shower_or_drying', models.BooleanField(default=True)),
                ('Details_Bath_or_shower_or_drying', models.CharField(blank=True, max_length=1000, null=True)),
                ('Grooming', models.BooleanField(default=True)),
                ('Details_Grooming', models.CharField(blank=True, max_length=1000, null=True)),
                ('Dressing', models.BooleanField(default=True)),
                ('Nail_care', models.BooleanField(default=True)),
                ('Other', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Supported_Accomodation', models.BooleanField(default=True)),
                ('Details_Supported_Accomodation', models.CharField(blank=True, max_length=1000, null=True)),
                ('NDIS_Plan_coordination', models.BooleanField(default=True)),
                ('Details_NDIS_Plan_coordination', models.CharField(blank=True, max_length=1000, null=True)),
                ('Community_access', models.BooleanField(default=True)),
                ('Details_Community_access', models.CharField(blank=True, max_length=1000, null=True)),
                ('Respite_care', models.BooleanField(default=True)),
                ('Details_Respite_care', models.CharField(blank=True, max_length=1000, null=True)),
                ('Transport', models.BooleanField(default=True)),
                ('Details_Transport', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Private_vehicle', models.BooleanField(default=True)),
                ('Details_Private_vehicle', models.CharField(blank=True, max_length=1000, null=True)),
                ('Taxi', models.BooleanField(default=True)),
                ('Details_Taxi', models.CharField(blank=True, max_length=1000, null=True)),
                ('Public_transport', models.BooleanField(default=True)),
                ('Details_Public_transport', models.CharField(blank=True, max_length=1000, null=True)),
                ('Other', models.BooleanField(default=True)),
                ('Details_Other', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='representative',
            name='Alternative_contact_person_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Email',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Landline',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Mobile',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Postal_address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='Residential_address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
