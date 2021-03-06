from django import forms
from django.contrib.auth.models import User
from basic_app.models import Userprofileinfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model = User
        fields = ['username','email','password']

class Userprofileinfoform(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ['portofolio','profile_pic']
