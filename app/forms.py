from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address', 'users_name', 'location', 'purchase_date']
class ComputerSearchForm(forms.Form):
    computer_name = forms.CharField(max_length=100, required=False)
    users_name = forms.CharField(max_length=100, required=False)
