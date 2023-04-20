from django.shortcuts import render
from datetime import datetime
def learn_django(request):
    # coursename = {'cname':'Django'}
    # cname = 'Django'
    # duration ='4 Months'
    # seats =10
    # django_details ={'n':cname,'du':duration,'st':seats}
    # d= datetime.now
    # student = {'names':['Rahul','Sonam','Raj','Anu']}

    data ={'stu1':{'name':'Rahul','roll':101},
          'stu2':{'name':'Sonam','roll':102},
          'stu3':{'name':'Raj','roll':103},
          'stu4':{'name':'Anu','roll':104},
        }
    # students = {'student':stu}  
    return render(request,'course/courseone.html',{'data':data})
def learn_python(request):
    return render(request,'course/coursetwo.html')