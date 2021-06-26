from django import forms

from .models import add
class  addnot(forms.ModelForm):
    class  Meta:
        model = add
        fields = ['title','desc']

