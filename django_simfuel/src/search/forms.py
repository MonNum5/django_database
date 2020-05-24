from django import forms

from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            #'searchDate',
            'user',
            'selectedDB',
            'search'
        ]
        '''
        widgets = {
                   'user': forms.HiddenInput(),
                   'selectedDB': forms.HiddenInput(),}
        '''
        
       
