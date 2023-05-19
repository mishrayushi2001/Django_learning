
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
  # name = forms.CharField(max_length=50,required= False)
  class Meta:
    model=User 
    fields = ['name','email','password']
    labels = {'name':'Enter Name','password':'Enter password',
    'email':'Enter Email',}
    # error_messages = {
    #   'name':{'required':'Write Name'},
    #   'password':{'required':'Write Password'},
    # }
    # widgets={'password':forms.PasswordInput,
    # 'name':forms.TextInput(attrs={'class':'myclass','placeholder':'yaha name likhiye'})}
    widgets={'password':forms.PasswordInput}
 
 