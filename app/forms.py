from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address', 'users_name', 'location', 'purchase_date']
class ComputerSearchForm(forms.Form):
    computer_name = forms.CharField(max_length=100, required=False)
    users_name = forms.CharField(max_length=100, required=False)
    
    def clean_computer_name(self): # Validates the Computer Name Field
        computer_name = self.cleaned_data.get('computer_name')
        if (computer_name == ""):
            raise forms.ValidationError('This field cannot be left blank')
        return computer_name

    def clean(self):
        cleaned_data = super().clean()
        computer_name = cleaned_data.get('computer_name')

        # Check for duplicate computer name
        if Computer.objects.filter(computer_name=computer_name).exists():
            raise forms.ValidationError(computer_name + ' is already added')

        return cleaned_data