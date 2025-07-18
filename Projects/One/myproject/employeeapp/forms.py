from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'email', 'department']