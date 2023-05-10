from django import forms
class StudentRegistration(forms.Form):
    # name = forms.CharField(initial="Sonam", help_text="is field me 30 char")
    name = forms.CharField(label='Your Name', label_suffix=' ', initial='Sonam', required=False, disabled=True,help_text='Limit 70 char')
    email = forms.EmailField(widget=forms.PasswordInput)
    # mobile = forms.IntegerField()
    # key = forms.CharField(widget=forms.HiddenInput())

    