from django import forms
from normalview.models import Messages

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['from_mail','message']