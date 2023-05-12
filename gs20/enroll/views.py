from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import StudentRegistration

def thankyou(request):
    return render(request,'enroll/success.html')
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
            return HttpResponseRedirect('/regi/success/')
            # return render(request, 'enroll/success.html',{'nm':name})
    else:
        fm = StudentRegistration()
        print("ye get request se aya h")        


    return render(request, 'enroll/userregistration.html',{'form':fm})

