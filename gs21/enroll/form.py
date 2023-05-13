from django import forms
class StudentRegistration(forms.Form):
    # name = forms.CharField(initial="Sonam", help_text="is field me 30 char")
    # name = forms.CharField(min_length=4,max_length=10,strip=True,
    # empty_value='Ayushi',error_messages={'required':'enter your name'})
    # roll = forms.IntegerField(min_value=6,max_value=40)
    # price = forms.FloatField(min_value=5, max_value=40)
    # rate = forms.FloatField(min_value=5, max_value=40)
    # comment =forms.SlugField()
    # email=forms.EmailField(min_length=5,max_length=50)
    # website=forms.URLField(min_length=5,max_length=50)
    # password = forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
    # description=forms.CharField(widget=forms.Textarea)
    # feedback=forms.CharField(min_length=5,max_length=50,widget = forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))
    # notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    # agree=forms.BooleanField(label_suffix='', label= 'I Agree')
    
    name = forms.CharField()
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return valname

