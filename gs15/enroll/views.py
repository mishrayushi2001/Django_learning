from django.shortcuts import render
from .form import StudentRegistration

def showformdata(request):
    fm = StudentRegistration(auto_id=True, label_suffix=' ',initial={
        'name':'Ayushi',
    })
    return render(request, 'enroll/userregistration.html',{'form':fm})

