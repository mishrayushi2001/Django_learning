from django import forms
class StudentRegistration(forms.Form):
    # name = forms.CharField(initial="Sonam", help_text="is field me 30 char")
    name = forms.CharField()
    email = forms.EmailField()
    
    