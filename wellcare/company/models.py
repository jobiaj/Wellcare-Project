from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from pytz import common_timezones

class WellCareUser(User):
    employee_id = models.CharField(max_length=1000,  null=True, blank=True)
    timezone = models.CharField(max_length=255, choices=[(x, x) for x in common_timezones], default='UTC')
    employee_info = models.ForeignKey('EmployeeInfo', blank=True, null=True)

    def add_user_info(self, user_info):
        self.employee_info = user_info
        self.save()



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
    existing_filled_form = models.FileField(upload_to='attachments',null=True, blank=True)

class ISP(models.Model):
    date = models.DateField()
    review_date = models.DateField()
    full_name = models.CharField(max_length=1000,  null=True, blank=True)
    date_of_birth = models.DateField()
    funding_choices = (
    (1, "NDIS"),
    (2, "Over 65"),
    (3, "Compensation"),
    (4, "Other")
)
    legal_status_choices = (
    (1, "Legally competent adult"),
    (2, "Competent adult with informed support"),
    (3, "Minor or adult with parent/relative as guardian"),
    (4, "Minor or adult with non-relative as guardian or legally appointed guardian"),
    (5, "Minor or adult with state as guardian")

)
    address = models.CharField(max_length=1000,  null=True, blank=True)
    funding = models.IntegerField(choices=funding_choices,default=1)
    medi_care_number = models.IntegerField(null=True)
    ndis_number = models.IntegerField(null=True)
    primary_disability = models.CharField(max_length=1000,  null=True, blank=True)
    secondary_disability = models.CharField(max_length=1000,  null=True, blank=True)
    gen_practitioner = models.CharField(max_length=1000,  null=True, blank=True)
    specialist = models.CharField(max_length=1000,  null=True, blank=True)
    legal_status = models.IntegerField(choices=legal_status_choices,default=1)

class Allergy(models.Model):
    Allergy = models.BooleanField(default=True)
    NIL = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Representative(models.Model):
    relationship_choices = (
    ("Parent", "Parent"),
    ("Sibling", "Sibling"),
    ("Legal Guardian", "Legal Guardian"),
    ("Financial Managers", "Financial Managers"),
    ("Other", "Other")
)
    full_name = models.CharField(max_length=1000,  null=True, blank=True)
    relationship = models.CharField(max_length=1000)
    Residential_address = models.CharField(max_length=1000,  null=True, blank=True)
    Postal_address = models.CharField(max_length=1000,  null=True, blank=True)
    Mobile = models.CharField(max_length=1000,  null=True, blank=True)
    Landline = models.CharField(max_length=1000,  null=True, blank=True)
    Email = models.CharField(max_length=1000,  null=True, blank=True)
    Alternative_contact_person_name = models.CharField(max_length=1000,  null=True, blank=True)
    relationship_choices_alternative_contact_person = (
    ("Parent", "Parent"),
    ("Sibling", "Sibling"),
    ("Legal Guardian", "Legal Guardian"),
    ("Financial Managers", "Financial Managers"),
    ("Other", "Other")
)
    Residential_address = models.CharField(max_length=1000,  null=True, blank=True)
    Postal_address = models.CharField(max_length=1000,  null=True, blank=True)
    Mobile = models.CharField(max_length=1000,  null=True, blank=True)
    Landline = models.CharField(max_length=1000,  null=True, blank=True)
    Email = models.CharField(max_length=1000,  null=True, blank=True)

class ServiceType(models.Model):
    Supported_Accomodation = models.BooleanField(default=True)
    Details_Supported_Accomodation = models.CharField(max_length=1000,  null=True, blank=True)
    NDIS_Plan_coordination = models.BooleanField(default=True)
    Details_NDIS_Plan_coordination = models.CharField(max_length=1000,  null=True, blank=True)
    Community_access = models.BooleanField(default=True)
    Details_Community_access = models.CharField(max_length=1000,  null=True, blank=True)
    Respite_care = models.BooleanField(default=True)
    Details_Respite_care = models.CharField(max_length=1000,  null=True, blank=True)
    Transport = models.BooleanField(default=True)
    Details_Transport = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Daily_routine(models.Model):
    Morning_routine = models.BooleanField(default=True)
    Details_Morning_routine = models.CharField(max_length=1000,  null=True, blank=True)
    Afternoon_routine = models.BooleanField(default=True)
    Details_Afternoon_routine = models.CharField(max_length=1000,  null=True, blank=True)
    Bed_time_routine = models.BooleanField(default=True)
    Details_Bed_time_routine = models.CharField(max_length=1000,  null=True, blank=True)
    General_daily_routine = models.BooleanField(default=True)
    Details_General_daily_routine = models.CharField(max_length=1000,  null=True, blank=True)
class General(models.Model):
    Communication = models.BooleanField(default=False)
    Details_Communication = models.CharField(max_length=1000,  null=True, blank=True)
    Decision_making = models.BooleanField(default=False)
    Details_Decision_making = models.CharField(max_length=1000,  null=True, blank=True)
    Cultural_background = models.BooleanField(default=True)
    Details_Cultural_background = models.CharField(max_length=1000,  null=True, blank=True)
    Language = models.BooleanField(default=True)
    Details_Language = models.CharField(max_length=1000,  null=True, blank=True)
    Nutrition_or_diet_or_weight = models.BooleanField(default=True)
    Details_Nutrition_or_diet_or_weight = models.CharField(max_length=1000,  null=True, blank=True)
    Vision = models.BooleanField(default=True)
    Details_Vision = models.CharField(max_length=1000,  null=True, blank=True)
    Hearing = models.BooleanField(default=True)
    Details_Hearing = models.CharField(max_length=1000,  null=True, blank=True)
    Speech = models.BooleanField(default=True)
    Details_Speech = models.CharField(max_length=1000,  null=True, blank=True)
    Financial_or_money = models.BooleanField(default=True)
    Details_Financial_or_money = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Medicle(models.Model):
    Medication_documentation = models.BooleanField(default=True)
    Details_Medication_documentation = models.CharField(max_length=1000,  null=True, blank=True)
    Medication = models.BooleanField(default=True)
    Details_Medication = models.CharField(max_length=1000,  null=True, blank=True)
    Medical_conditions = models.BooleanField(default=True)
    Details_Medical_conditions = models.CharField(max_length=1000,  null=True, blank=True)
    Seizure_management_plan = models.BooleanField(default=True)
    Details_Seizure_management_plan = models.CharField(max_length=1000,  null=True, blank=True)
    Bowel_management_plan = models.BooleanField(default=True)
    Details_Bowel_management_plan = models.CharField(max_length=1000,  null=True, blank=True)
    PEG  = models.BooleanField(default=True)
    Details_PEG = models.CharField(max_length=1000,  null=True, blank=True)
    Infectious_diseases = models.BooleanField(default=True)
    Has_Client_had_chicken_fox = models.BooleanField(default=True)
    Has_Client_had_Hepatitis_A_B_C_orD = models.BooleanField(default=True)
    Other = models.CharField(max_length=1000,  null=True, blank=True)
    Immunization = models.BooleanField(default=True)
    Triple_antigen_Date = models.BooleanField(default=True)
    Sabin_Date = models.BooleanField(default=True)
    TetanusDate = models.BooleanField(default=True)
    Other = models.BooleanField(default=True)
    Medical_appointments = models.BooleanField(default=True) 
    Details_Medical_appointments = models.CharField(max_length=1000,  null=True, blank=True)
    Advanced_care_plan = models.BooleanField(default=True)
    Details_Advanced_care_plan = models.CharField(max_length=1000,  null=True, blank=True)
    Nursing_support = models.BooleanField(default=True)
    Details_Nursing_support = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class PersonalCare(models.Model):
    Hygiene =  models.BooleanField(default=True)
    Details_Hygiene = models.CharField(max_length=1000,  null=True, blank=True)
    Pressure_care =  models.BooleanField(default=True)
    Details_Pressure_care = models.CharField(max_length=1000,  null=True, blank=True)
    Bladder_care =  models.BooleanField(default=True)
    Details_Bladder_care = models.CharField(max_length=1000,  null=True, blank=True)
    Bowel_care = models.BooleanField(default=True)
    Details_Bowel_care = models.CharField(max_length=1000,  null=True, blank=True)
    Toileting = models.BooleanField(default=True)
    Details_Toileting = models.CharField(max_length=1000,  null=True, blank=True)
    Menstrual_management = models.BooleanField(default=True)
    Details_Menstrual_management = models.CharField(max_length=1000,  null=True, blank=True)
    Positioning = models.BooleanField(default=True)
    Details_Positioning = models.CharField(max_length=1000,  null=True, blank=True)
    Meal_assistance = models.BooleanField(default=True)
    Details_Meal_assistance = models.CharField(max_length=1000,  null=True, blank=True)
    Oral_care = models.BooleanField(default=True)
    Details_Oral_care = models.CharField(max_length=1000,  null=True, blank=True)
    Bath_or_shower_or_drying = models.BooleanField(default=True)
    Details_Bath_or_shower_or_drying = models.CharField(max_length=1000,  null=True, blank=True)
    Grooming = models.BooleanField(default=True)
    Details_Grooming = models.CharField(max_length=1000,  null=True, blank=True)
    Dressing = models.BooleanField(default=True)
    Nail_care = models.BooleanField(default=True)
    Other = models.BooleanField(default=True)
class Mobility(models.Model):
    Weight_bear = models.BooleanField(default=True)
    Details_Weight_bear = models.CharField(max_length=1000,  null=True, blank=True)
    Stand_transfer = models.BooleanField(default=True)
    Details_Stand_transfer = models.CharField(max_length=1000,  null=True, blank=True)
    Hoist_transfer = models.BooleanField(default=True)
    Details_Hoist_transfer = models.CharField(max_length=1000,  null=True, blank=True)
    Walking_or_running = models.BooleanField(default=True)
    Details_Walking_or_running = models.CharField(max_length=1000,  null=True, blank=True)
    Positioning = models.BooleanField(default=True)
    Details_Positioning = models.CharField(max_length=1000,  null=True, blank=True)
    Exercise = models.BooleanField(default=True)
    Details_Exercise = models.CharField(max_length=1000,  null=True, blank=True)
    WHS_issues_or_manual_handling = models.BooleanField(default=True)
    Details_WHS_issues_or_manual_handling = models.CharField(max_length=1000,  null=True, blank=True)
    Wheel_chair = models.BooleanField(default=True)
    Details_Wheel_chair = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Equipment_and_aids(models.Model):
    Equipment_or_aids_required = models.BooleanField(default=True)
    Details_Equipment_or_aids_required = models.CharField(max_length=1000,  null=True, blank=True)
    Wheel_chair = models.BooleanField(default=True)
    Details_Wheel_chair = models.CharField(max_length=1000,  null=True, blank=True)
    Walking_frame_stick = models.BooleanField(default=True)
    Details_Walking_frame_stick = models.CharField(max_length=1000,  null=True, blank=True)
    Shower_chair = models.BooleanField(default=True)
    Details_Shower_chair = models.CharField(max_length=1000,  null=True, blank=True)
    Communication = models.BooleanField(default=True)
    Details_Communication = models.CharField(max_length=1000,  null=True, blank=True)
    Assistive_technology = models.BooleanField(default=True)
    Details_Assistive_technology = models.CharField(max_length=1000,  null=True, blank=True)
    Maintenance_of_equipment = models.BooleanField(default=True)
    Details_Maintenance_of_equipment = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Behaviour(models.Model):
    Behavior_management = models.BooleanField(default=True)
    Details_Behavior_management = models.CharField(max_length=1000,  null=True, blank=True)
    Community_support = models.BooleanField(default=True)
    Details_Community_support = models.CharField(max_length=1000,  null=True, blank=True)
    Supervision = models.BooleanField(default=True)
    Details_Supervision = models.CharField(max_length=1000,  null=True, blank=True)
    Time_management = models.BooleanField(default=True)
    Details_Time_management = models.CharField(max_length=1000,  null=True, blank=True)
    Transport_or_vehicle = models.BooleanField(default=True)
    Details_Transport_or_vehicle = models.CharField(max_length=1000,  null=True, blank=True)
    Triggers = models.BooleanField(default=True)
    Details_Triggers = models.CharField(max_length=1000,  null=True, blank=True)
    Communication = models.BooleanField(default=True)
    Details_Communication = models.CharField(max_length=1000,  null=True, blank=True)
    Routine = models.BooleanField(default=True)
    Details_Routine = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Household_tasks(models.Model):
    Shopping =models.BooleanField(default=True)
    Details_Shopping = models.CharField(max_length=1000,  null=True, blank=True)
    Kitchen_or_meal_preparation = models.BooleanField(default=True)
    Details_Kitchen_or_meal_preparation = models.CharField(max_length=1000,  null=True, blank=True)
    Laundry = models.BooleanField(default=True)
    Details_Laundry = models.CharField(max_length=1000,  null=True, blank=True)
    Cleaning_or_room_maintenance = models.BooleanField(default=True)
    Details_Cleaning_or_room_maintenance = models.CharField(max_length=1000,  null=True, blank=True)
    Gardening = models.BooleanField(default=True)
    Details_Gardening = models.CharField(max_length=1000,  null=True, blank=True)
    Pet_or_animal_care = models.BooleanField(default=True)
    Details_Pet_or_animal_care = models.CharField(max_length=1000,  null=True, blank=True)
    Phone_or_mail_or_computer = models.BooleanField(default=True)
    Details_Phone_or_mail_or_computer = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)
class Transport(models.Model):
    Private_vehicle = models.BooleanField(default=True)
    Details_Private_vehicle = models.CharField(max_length=1000,  null=True, blank=True)
    Taxi = models.BooleanField(default=True)
    Details_Taxi = models.CharField(max_length=1000,  null=True, blank=True)
    Public_transport = models.BooleanField(default=True)
    Details_Public_transport = models.CharField(max_length=1000,  null=True, blank=True)
    Other = models.BooleanField(default=True)
    Details_Other = models.CharField(max_length=1000,  null=True, blank=True)