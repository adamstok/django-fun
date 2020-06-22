from django import forms
from django.forms import Form


class RenterSearchForm(forms.Form):
    query = forms.CharField(required=False)

