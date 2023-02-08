from django import forms
from .models import InsuranceList, VisitorData, Car


class ProductSelectionForm(forms.Form):
    '''This form is used to select the product/s that the user wants to quote.
       Is important to note that the user can select more than one product
    '''
    products = forms.ModelMultipleChoiceField(queryset=InsuranceList.objects.all(), widget=forms.CheckboxSelectMultiple)

class QuoteForm(forms.Form):
    '''This form is used to get the name, surname and email of the user'''
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    phone_prefix = forms.CharField(max_length=5)
    phone_number = forms.CharField(max_length=20)

class CarForm(forms.Form):
    '''This form is used to get the car information'''
    Marca = forms.CharField(max_length=100)
    Modelo = forms.CharField(max_length=150)
    Año = forms.IntegerField()
    Version = forms.CharField(max_length=200)
    Tiene_gnc = forms.BooleanField(required=False)
    is_new = forms.BooleanField(required=False)
    
class HouseForm(forms.Form):
    '''
    This form is used to get the house information
    '''
    metros_cuadrados_cubiertos = forms.IntegerField()
    tipo_de_vivienda = forms.CharField(max_length=100)

