from django import forms
from .models import *


class GetInfoForm(forms.Form):
    number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    oms = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))