from django.core import validators
from django import forms
from .models import Employee


class EmployeeDetails(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "email", "salary", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
        }