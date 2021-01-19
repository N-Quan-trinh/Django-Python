from django import forms
from myWeb.models import UserAccount
from django.http import HttpResponseRedirect


class ModelRegister(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('UserName', 'Password', 'email', 'RealName')


class ModelLogin(forms.Form):
    UserName = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50)



