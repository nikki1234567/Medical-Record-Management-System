from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .forms import PostForm2
from .models import  Upload_prescription
from .models import  Upload_reports
def temporary_files(request):
    prescriptions  = Upload_prescription.objects.all()
    reports =  Upload_reports.objects.all()
    return render(request,'uploads/files.html',{'prescriptions':prescriptions,'reports':reports})




def uploads(request):

    if request.method == 'POST':
        print(request.POST)
        details = PostForm(request.POST,request.FILES)
        details2 = PostForm2(request.POST,request.FILES)
        if details.is_valid():
            post=details.save(commit=False)
            post.save()
            return HttpResponse("data for reports is submitted successfully")
        elif details2.is_valid():
            post2 = details2.save(commit=False)
            post2.save()
            return HttpResponse("data for prescriptions submitted successfully")
        else:
            return HttpResponse("None of the forms are filled!")
    else:
        return render(request,'uploads/upload.html')



   

        



    
