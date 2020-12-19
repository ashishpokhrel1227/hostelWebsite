from django.forms import ModelForm
from django import forms
from hostel.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'first_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'middle_name'}),
            'last_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'last_name'}),
            'address': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'contactus', 'type': 'number', 'placeholder': 'phone_no'}),
            'room': forms.Select(attrs={'class': 'contactus'})
        }