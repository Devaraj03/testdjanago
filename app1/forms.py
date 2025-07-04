from django import forms
from .models import *

class ComicsForm(forms.ModelForm):
    class Meta:
        model=comics
        fields=['title','author','img','description']
    
