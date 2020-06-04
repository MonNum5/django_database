from django import forms
from .models import notebook

class notebookForm(forms.ModelForm):
    class Meta:
        model = notebook
        fields = [
            'name',
            'file',
            'description'
        ]