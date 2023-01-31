from django import forms
from .models import InsuranceList, Quote, Car


class ProductSelectionForm(forms.Form):
    '''This form is used to select the product/s that the user wants to quote.
       Is important to note that the user can select more than one product
    '''
    product = forms.ModelMultipleChoiceField(queryset=InsuranceList.objects.all(), widget=forms.CheckboxSelectMultiple)

class QuoteForm(forms.Form):
    '''This form is used to get the name, surname and email of the user'''
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    phone_prefix = forms.CharField(max_length=5)
    phone_number = forms.CharField(max_length=20)

class CarForm(forms.Form):
    '''
    This form is the form just when the ProductSelectionForm is car insurance
    '''
    car_brand = forms.CharField(max_length=100)
    car_model = forms.CharField(max_length=100)
    car_year = forms.CharField(max_length=4)
    car_version = forms.CharField(max_length=100)
    has_gnc = forms.BooleanField()
    is_it_new = forms.BooleanField()

class HouseForm(forms.Form):
    '''
    This form is the form just when the ProductSelectionForm is house insurance
    '''
    pass
    