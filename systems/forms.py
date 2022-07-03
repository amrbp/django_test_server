from django import forms

from systems.models import *

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        fields = "__all__"
