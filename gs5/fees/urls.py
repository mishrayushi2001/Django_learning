from django.urls import path
from fees import views
from django.contrib import admin


urlpatterns = [  
    path('feesdj/',views.fees_django),
    path('feespy/',views.fees_python),

    ]