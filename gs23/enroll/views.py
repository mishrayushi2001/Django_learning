from django.shortcuts import render
from .form import StudentRegistration
from .models import User

def showformdata(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # reg = User(name=nm, email=em, password=pw)

            # reg = User(id=1, name=nm, email=em, password=pw)
            # reg.save()
            reg = User(id=1)
            reg.delete()
    else:
        fm = StudentRegistration()
        print("ye get request se aya h")        

    return render(request, 'enroll/userregistration.html',{'form':fm})

