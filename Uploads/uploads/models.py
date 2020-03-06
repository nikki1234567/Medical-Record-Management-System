from django.db import models
from django.utils import timezone
# Create your models here.

#model for prescriptions
class Upload_prescription(models.Model):
    hospital_name = models.CharField( max_length=50,blank=False,null=False)
    disease_name = models.CharField(max_length=15,blank=False,null=False)
    file_name = models.CharField(max_length=15,blank=False,null=False,default="Some Name")
    prescription_file = models.FileField(upload_to='files/prescriptions',default="Some File")

    def __str__(self):
        return self.hospital_name
    
#model for reports
class Upload_reports(models.Model):
    diagnostics_name = models.CharField(max_length=50,blank=False,null=False)
    report_type = models.CharField(max_length=20,blank=False,null=False)
    file_name = models.CharField(max_length=15,blank=False,null=False,default="Some Name")
    date = models.DateField()
    report_file = models.FileField(upload_to='files/reports',default="Some File")


