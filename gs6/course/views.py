from django.shortcuts import render
from datetime import datetime
def learn_django(request):
    # coursename = {'cname':'Django'}
    # cname = 'Django'
    # duration ='4 Months'
    # seats =10
    # django_details ={'n':cname,'du':duration,'st':seats}
    # d= datetime.now
    return render(request,'course/courseone.html',{'nm':'Django','st':5})
def learn_python(request):
    return render(request,'course/coursetwo.html')