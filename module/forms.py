from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    empid = forms.CharField(max_length=10)  # Assuming 'empid' is a CharField with max_length 10
    role = forms.CharField(max_length=50)   # Assuming 'role' is a CharField with max_length 50

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'empid', 'role', 'password']

