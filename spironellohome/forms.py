from django import forms
from .models import InsuranceList, VisitorData, Car

class ProductSelectionForm(forms.Form):
    '''This form is used to select the product/s that the user wants to quote.
       Is important to note that the user can select more than one product
    '''
    products = forms.ModelMultipleChoiceField(queryset=InsuranceList.objects.all(), widget=forms.CheckboxSelectMultiple)


class CarForm(forms.Form):
    '''This form is used to get the car information'''
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=150)
    año = forms.IntegerField()
    version = forms.CharField(max_length=200)
    tiene_gnc = forms.BooleanField(required=False)
    es_nuevo = forms.BooleanField(required=False)
    
class HouseForm(forms.Form):
    '''
    This form is used to get the house information
    '''
    metros_cuadrados_cubiertos = forms.IntegerField()
    tipo_de_vivienda = forms.CharField(max_length=100)

class BasePjForms(forms.Form):
    '''
    Pj stands for Persona Juridica, which means legal person
    This form is used to get business information. It's enough
    for the ART form
    The reason of its existence is to avoid fields repetition
    '''
    razon_social = forms.CharField(max_length=200)
    cuit = forms.CharField(max_length=22)

class BusinessForm(BasePjForms):
    '''
    this is for business insurance. Also known as seguro de comercio
    '''
    metros_cuadrados_cubiertos = forms.IntegerField()
    actividad = forms.CharField(max_length=200)

class TripForm(forms.Form):
    '''
    This form is used to get the trip information to quote
    '''
    origen = forms.CharField(max_length=200)
    destino = forms.CharField(max_length=200)
    fecha_de_salida = forms.DateField()
    fecha_de_regreso = forms.DateField()
    cantidad_de_pasajeros = forms.IntegerField()

class CaucionForm(forms.Form):
    '''
    This form is used to get the caucion information to quote
    '''
    tipo_de_caucion = forms.CharField(max_length=200)
    comentarios_adicionales = forms.CharField(max_length=200)

class QuoteForm(forms.Form):
    '''This form is used to get the name, surname and email of the user'''
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    phone_prefix = forms.CharField(max_length=5)
    phone_number = forms.CharField(max_length=20)
