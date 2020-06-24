from django import forms
from django.forms import Form
from handling.models import Apartments,ApartmentsPics


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

class ApartmentsForm(forms.ModelForm):
    class Meta:
        model = Apartments
        fields = "__all__"

class ImageUploadForm1(forms.Form):
    image = forms.ImageField()
    apartment = forms.ModelChoiceField(Apartments.objects.all())


class ImageUploadForm(forms.Form):
    class Meta:
        model = ApartmentsPics
        fields = "__all__"