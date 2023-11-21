from django import forms
from .models import Faculty

class FacultyAddForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name', 'last_name', 'email', 'academic_rank']

class FacultyEditForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name', 'last_name', 'email', 'academic_rank']