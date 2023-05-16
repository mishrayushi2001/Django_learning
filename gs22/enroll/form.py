
from django.core import validators
from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email=forms.EmailField(error_messages={'required':'Enter Your Email'},min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your password'},min_length=5, max_length=50)
    rpassword = forms.CharField(label='Password(again)',widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd=self.cleaned_data['password']
    #     valrpwd =self.cleaned_data['rpassword']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('Password does not match')
   




