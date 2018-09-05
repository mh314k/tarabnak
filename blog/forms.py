# coding=utf-8
from django import forms

class commentform(forms.Form):
    CommenterName = forms.CharField(
        max_length=200,
        label='نام شما',
    )
