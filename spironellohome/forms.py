from django import forms
from .models import MarketPlaceProducts

class ProductSelectionForm(forms.Form):
    product = forms.ModelMultipleChoiceField(queryset=MarketPlaceProducts.objects.all())
    