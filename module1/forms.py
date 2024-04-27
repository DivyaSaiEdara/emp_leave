from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'reason']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add specifications for start date field
        self.fields['start_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        self.fields['start_date'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['start_date'].label = 'Start Date'

        # Add specifications for end date field
        self.fields['end_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        self.fields['end_date'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['end_date'].label = 'End Date'
