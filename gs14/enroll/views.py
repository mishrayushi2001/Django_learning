from django.shortcuts import render
from .form import StudentRegistration

def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html',{'form':fm})

