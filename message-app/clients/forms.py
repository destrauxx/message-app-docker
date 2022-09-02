from unicodedata import name
from django import forms

from .models import Client
import re

class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'name',
            'last_name',
        ]

    def save(self, commit=True):
        instance = super(CreateClientForm, self).save(commit=False)
        if not re.match(r"Mrs.", instance.name):
            instance.name = "Mrs. " + instance.name
        return instance
        # widgets = {
        #     'header': forms.TextInput(attrs={'placeholder': 'Note header'}),
        # }