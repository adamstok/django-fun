from django import forms
from django.forms import Form
from handling.models import Apartments


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

class ApartmentsForm(forms.ModelForm):
    class Meta:
        model = Apartments
        fields = "__all__"

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
