# forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        
    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')
        # Add any additional validation or cleaning logic here
        return zipcode
