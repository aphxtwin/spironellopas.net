from django.urls import path
from . import views
from .views import QuoteSelectionView, IndexView, MarketplaceView, ProductDetailView, LearningView, DetailedArticle
from .forms import ProductSelectionForm,QuoteForm, CarForm, HouseForm


urlpatterns = [
    path("", IndexView.as_view() , name="index"),
    path("learning",LearningView.as_view(), name="learning"),
    path("learning/<slug:slug>", DetailedArticle.as_view(), name="detailed_article"),
    path("cotizacion", QuoteSelectionView.as_view(), name='quickquote'),
    path("marketplace", MarketplaceView.as_view(), name="marketplace"),
    path("marketplace/<slug:slug>", ProductDetailView.as_view(), name= 'product_detail')
]
