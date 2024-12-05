from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number','first_name','last_name','email','field_of_study','gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study':'Field of Study',
            'gpa': 'GPA'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'formcontrol'}),
            'first_name': forms.TextInput(attrs={'class': 'formcontrol'}),
            'last_name': forms.TextInput(attrs={'class': 'formcontrol'}),
            'email': forms.EmailInput(attrs={'class': 'formcontrol'}),
            'field_of_study': forms.TextInput(attrs={'class': 'formcontrol'}),
            'gpa': forms.NumberInput(attrs={'class': 'formcontrol'})
        }