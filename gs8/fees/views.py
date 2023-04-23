from django.shortcuts import render

def fees_django(request):
    return render(request, 'fees/feesone.html',{'title':'Django Fees','cname':'Django','charge':300})
     
 