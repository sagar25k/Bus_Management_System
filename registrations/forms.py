# registrations/forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'student', 
            'parent_name', 
            'student_mobileno', 
            'parent_mobileno', 
            'student_address', 
            'branch', 
            'boarding_location', 
            'destination', 
            'confirmation'
        ]
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),  # Assuming it's a foreign key to Student model
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter parent name'}),
            'student_mobileno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student mobile number'}),
            'parent_mobileno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter parent mobile number'}),
            'student_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter student address', 'rows': 3}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch'}),
            'boarding_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter boarding location'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination'}),
            'confirmation': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')], attrs={'class': 'form-control'}),
        }
