from django.shortcuts import render

def learn_django(request):
    # coursename = {'cname':'Django'}
    cname = 'Django'
    duration ='4 Months'
    seats =10
    django_details ={'n':cname,'du':duration,'st':seats}
    return render(request,'course/courseone.html',context=django_details)
def learn_python(request):
    return render(request,'course/coursetwo.html')