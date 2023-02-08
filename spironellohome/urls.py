from django.urls import path
from . import views
from .views import QuoteWizardView, IndexView, MarketplaceView, ProductDetailView
from .forms import ProductSelectionForm,QuoteForm, CarForm, HouseForm


urlpatterns = [
    path("", IndexView.as_view() , name="index"),
    path("cotizacion", QuoteWizardView.as_view(), name='quickquote'),
    path("marketplace", MarketplaceView.as_view(), name="marketplace"),
    path("marketplace/<slug:slug>", ProductDetailView.as_view(), name= 'product_detail')
]
