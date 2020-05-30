from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userModel
from databases. models import database
from .models import userModel
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


from multiselectfield import MultiSelectFormField
from .models import userModel
class AdditionalUserForm(forms.Form):

    fields = MultiSelectFormField(choices=userModel.choices)


        

    

