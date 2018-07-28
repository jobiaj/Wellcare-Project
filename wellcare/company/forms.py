from django.forms.models import modelform_factory, modelformset_factory
from models import EmployeeInfo
UserInfoForm = modelform_factory(EmployeeInfo, fields='__all__')