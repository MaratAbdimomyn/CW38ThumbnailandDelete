from django import forms
from django.forms import ModelForm
from .models import *

class CarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('brand', 'name', 'cars_image', 'file')