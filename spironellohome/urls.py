from django.urls import path
from . import views
from .views import QuoteWizardView
from .forms import ProductSelectionForm,QuoteForm, CarForm

urlpatterns = [
    path("", views.index, name="index"),
    path("cotizacion", QuoteWizardView.as_view([ProductSelectionForm,QuoteForm]), name='quickquote'),
    path("marketplace", views.marketplace, name="marketplace"),
    path("marketplace/<slug:slug>", views.product_detail, name= 'product_detail')
]
