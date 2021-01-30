from django import forms
from myWeb.models import UserAccount
from django.http import HttpResponseRedirect


class ModelRegister(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('UserName', 'Password', 'email', 'RealName')
        widgets = {
            'UserName': forms.TextInput(attrs={'placeholder': 'UserName'}),
            'Password': forms.TextInput(attrs={'placeholder': 'Password'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'RealName': forms.TextInput(attrs={'placeholder': 'Real Name'})
        }


class ModelLogin(forms.Form):
    UserName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    Password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Password'}))
