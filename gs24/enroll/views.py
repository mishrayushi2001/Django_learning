from django.shortcuts import render
from .form import StudentRegistration
from .models import User

def showformdata(request):
    if request.method =='POST':
        pi = User.objects.get()
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            # nm = fm.cleaned_data['name']
            # em = fm.cleaned_data['email']
            # pw = fm.cleaned_data['password']
            # reg = User(name=nm,email=em,password=pw)
            # reg.save()
            # print(nm)
            # print(em)
            # print(pw)
    else:
        fm = StudentRegistration()  
        print("ye get request se aya h")        

    return render(request, 'enroll/userregistration.html',{'form':fm})

