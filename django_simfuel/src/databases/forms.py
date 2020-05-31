from django import forms

from .models import database

class dataBaseForm(forms.ModelForm):
    class Meta:
        model = database
        fields = '__all__'

class dataBaseFormUpdate(forms.ModelForm):
    class Meta:
        model = database
        fields = '__all__'
        exclude = ('dbAbbreviation',)