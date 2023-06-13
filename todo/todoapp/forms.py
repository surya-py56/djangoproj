from django import forms
from todoapp.models import Product

class EmpForms(forms.Form):
    name=forms.CharField(max_length=50)
    sal=forms.FloatField()
    city=forms.CharField(max_length=20)

class ProdForms(forms.ModelForm):
    pname=forms.CharField(max_length=50)
    pdesc=forms.CharField(max_length=500)
    price=forms.FloatField()
    class Meta:
        model=Product
        fields=['pname','pdesc','price']