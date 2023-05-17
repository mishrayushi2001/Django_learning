
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
  class Meta:
    model=User 
    fields = ['name','email','password']
    labels = {'name':'Enter Name','password':'Enter password',
              'email':'Enter Email',}
    error_messages = {
      'name':{'required':'Write Name'},
      'password':{'required':'Write Password'},
    }
    widgets={'password':forms.PasswordInput,
             'name':forms.TextInput(attrs={'class':'myclass','placeholder':'yaha name likhiye'})}

 