from django import forms 
from clinicalsApp.models import Patient, ClinicalData, Doctor, Visit

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = '__all__'

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'