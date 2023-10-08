from django import forms
from .models import *

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'operating_system','MAC_address', 'users_name', 'location', 'purchase_date']

class ComputerSearchForm(forms.Form):
    computer_name = forms.CharField(max_length=100, required=False)
    users_name = forms.CharField(max_length=100, required=False)
    export_to_CSV = forms.BooleanField(required=False, label="Export to CSV")


class OSForm(forms.ModelForm):
    class Meta:
        model = operating_system
        fields = ['name']
