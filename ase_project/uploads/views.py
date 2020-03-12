from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .forms import PostForm2
from .models import  Upload_prescription
from .models import  Upload_reports
from django.contrib import messages

def home(request):
    return render(request, 'uploads/homepage.html',{'title':'Home'})

def forum(request):
    return render(request,'uploads/forums.html',{'title':'Forum'})

def remainder(request):
    return render(request,'uploads/project.html',{'title':'Remainder'})

def uploads(request):

    if request.method == 'POST':
        print(request.POST)
        details = PostForm(request.POST,request.FILES)
        details2 = PostForm2(request.POST,request.FILES)
        if details.is_valid():
            post=details.save(commit=False)
            post.save()
            messages.success(request,"Data for Prescription Submitted Succesfully..!!")
            return redirect('Upload')
        elif details2.is_valid():
            post2 = details2.save(commit=False)
            post2.save()
            messages.success(request,"Data for Report Submitted Succesfully..!!")
            return redirect('Upload')
        else:
            return HttpResponse("None of the forms are filled!")
    else:
        return render(request,'uploads/upload.html',{'title':'Uploads'})


def temporary_files(request):
    prescriptions= Upload_prescription.objects.all()
    reports =Upload_reports.objects.all()
    return render(request,'uploads/files.html',{'prescriptions':prescriptions,'reports':reports})

def delete_prescription(request, pk):
    if request.method == 'POST':
        file = Upload_prescription.objects.get(id=pk)
        file.delete()
    return redirect('/files')

def delete_report(request, pk):
    if request.method == 'POST':
        file = Upload_reports.objects.get(id=pk)
        file.delete()
    return redirect('/files')

def searchprescription(request):
    prescription= Upload_prescription.objects.all()
    hospital_name_query = request.GET.get('hospital_name')
    disease_name_query = request.GET.get('disease_name')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if hospital_name_query != '' and hospital_name_query is not None:
        prescription = prescription.filter(hospital_name__icontains = hospital_name_query)

    if disease_name_query != '' and disease_name_query is not None:
        prescription = prescription.filter(disease_name__icontains = disease_name_query)

    if date_min != '' and date_min is not None:
        prescription = prescription.filter(date__gte=date_min)

    if date_max != '' and date_max is not None:
        prescription = prescription.filter(date__lt=date_max)
    context = {
        'prescriptions':prescription,
        }
    return render(request,'uploads/prescriptionsearch.html',context)


def searchreport(request):
    report= Upload_reports.objects.all()
    diagnostics_name_query = request.GET.get('diagnostics_name')
    report_type_query = request.GET.get('report_type')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    if diagnostics_name_query != '' and diagnostics_name_query is not None:
        report = report.filter(diagnostics_name__icontains = diagnostics_name_query)
    if report_type_query != '' and report_type_query is not None:
        report = report.filter(report_type__icontains = report_type_query)
    if date_min != '' and date_min is not None:
        report = report.filter(date__gte=date_min)
    if date_max != '' and date_max is not None:
        report = report.filter(date__lt=date_max)
    context = {
        'reports':report,
        }
    return render(request,'uploads/reportsearch.html',context)



    
