from django.shortcuts import render
from .models import MarketPlaceProducts
# Create your views here.

def index(request):
    return render(request, 'spironellohome/homepage.html')

def marketplace(request):
    products = MarketPlaceProducts.objects.all() 
    context = {
        'products': products
    }
    return render(request, 'spironellohome/marketplace.html', context)
