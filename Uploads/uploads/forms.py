from django import forms
from django.forms import ModelForm

from uploads.models import Upload_prescription,Upload_reports 

class PostForm(ModelForm):
    class Meta:
        model=Upload_prescription 
        fields=['hospital_name','disease_name','file_name','prescription_file']

class PostForm2(ModelForm):
    class Meta:
        model = Upload_reports
        fields=['diagnostics_name','report_type','file_name','date','report_file']        


