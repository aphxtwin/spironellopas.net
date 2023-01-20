from django import forms
from .models import MarketPlaceProducts

class ProductSelectionForm(forms.Form):
    product = forms.ModelMultipleChoiceField(queryset=MarketPlaceProducts.objects.all())

class NameSurnameEmail(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)