from django.shortcuts import render
from .form import StudentRegistration

def showformdata(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
            print('Password:',fm.cleaned_data['password'])
            print('Rpassword:',fm.cleaned_data['rpassword'])
    else:
        fm = StudentRegistration()
        print("ye get request se aya h")        


    return render(request, 'enroll/userregistration.html',{'form':fm})

