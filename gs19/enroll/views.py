from django.shortcuts import render
from .form import StudentRegistration

def showformdata(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            name=request.POST['name']
            email= fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print('Name', name) 
            print('Email', email) 
            print('password',password)  
        fm = StudentRegistration()
         
    else:
        fm = StudentRegistration()
        print("ye get request se aya h")        


    return render(request, 'enroll/userregistration.html',{'form':fm})

